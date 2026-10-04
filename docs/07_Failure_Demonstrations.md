# Phase 1 Failure Demonstrations and Recovery

Five failure scenarios were tested on 3 October 2026. Each test isolated a fault, recorded its effect and verified recovery.

## 1. Project Machines

| Member | Role | Address |
|---|---|---|
| Nitin | Private DNS and Backend A | 10.63.169.3; backend port 3001 |
| Kartik | nginx edge | 10.63.169.72; HTTPS port 8443 |
| Piyush | Backend B and test client | 10.63.169.63; backend port 3002 |

Working project domain:

```text
https://app.teamcn.test:8443/api/status
```

## 2. Results Summary

| Fault | Observed Result | Recovery |
|---|---|---|
| Wrong client DNS | NXDOMAIN; edge IP ping still worked | Private DNS restored; correct resolution returned |
| Wrong DNS record IP | NOERROR with incorrect IP; connection refused | Correct record restored; HTTP 200 returned |
| Backend A stopped | Six HTTP 200 responses from B | Responses from A and B returned |
| Both backends stopped | DNS and TLS worked; nginx returned 502 | Six HTTP 200 responses after recovery |
| Wrong destination port | DNS worked; TCP connection refused | Correct port returned HTTP 200 |

## 3. Wrong Client DNS

### Before

Piyush used private DNS server `10.63.169.3`. The domain `app.teamcn.test` resolved to the correct nginx edge IP `10.63.169.72`.

### Fault Introduced — Piyush

```bash
sudo networksetup -setdnsservers "Wi-Fi" 8.8.8.8
networksetup -getdnsservers "Wi-Fi"
dig app.teamcn.test A +time=3 +tries=1
ping -c 4 10.63.169.72
```

### Observed Result

The DNS query returned:

```text
status: NXDOMAIN
ANSWER: 0
SERVER: 8.8.8.8#53(8.8.8.8)
```

The IP ping still returned:

```text
4 packets transmitted, 4 packets received, 0.0% packet loss
```

### Layer Affected

Application-layer DNS name resolution failed because the public resolver did not resolve our private project domain.

IP connectivity remained available, as demonstrated by the successful ping.

### Failure Screenshot

![Wrong DNS produces NXDOMAIN while IP ping succeeds](../evidence/Piyush_failure_wrong_DNS.jpg)

### Restoration — Piyush

```bash
sudo networksetup -setdnsservers "Wi-Fi" 10.63.169.3
networksetup -getdnsservers "Wi-Fi"
dig app.teamcn.test A +time=3 +tries=1
```

The query returned `NOERROR`, answer `10.63.169.72`, and DNS server `10.63.169.3#53`.

![Private DNS restored successfully](../evidence/Piyush_restore_DNS.jpg)

## 4. Wrong DNS Record IP

### Before

The working DNS record was:

```conf
host-record=app.teamcn.test,10.63.169.72
```

### Fault Introduced — Nitin

Nitin backed up the DNS configuration, stopped the project dnsmasq process and changed the app record to:

```conf
host-record=app.teamcn.test,10.63.169.3
```

The incorrect configuration passed syntax validation and was started for the test.

### Client Test — Piyush

```bash
sudo dscacheutil -flushcache
sudo killall -HUP mDNSResponder

dig app.teamcn.test A +time=3 +tries=1

curl -v --connect-timeout 5 --max-time 10 \
  https://app.teamcn.test:8443/api/status
```

### Observed Result

DNS returned `NOERROR`, but the answer was the incorrect IP `10.63.169.3`.

Curl attempted to connect to `10.63.169.3:8443` and returned `Connection refused`, because nginx HTTPS was running on Kartik's Mac instead.

### Layer Affected

The DNS configuration returned incorrect application-layer naming information. The subsequent TCP connection targeted the wrong machine, where port 8443 had no listening service.

A successful DNS response alone does not establish that the returned address is correct.

### Restoration

Nitin stopped the test DNS process, restored the working configuration from its backup, validated it and restarted dnsmasq.

Piyush flushed the resolver cache and repeated the tests.

Recorded recovery:

```text
DNS status: NOERROR
app.teamcn.test. 60 IN A 10.63.169.72
HTTP/1.1 200 OK
X-Backend: A
```

## 5. Backend A Stopped

### Before

Both backends were running and requests through nginx had returned responses from A and B.

### Fault Introduced — Nitin

Nitin pressed Ctrl+C in Backend A's terminal, stopping the service on port `3001`.

### Client Test — Piyush

```bash
for i in 1 2 3 4 5 6; do
  printf '\nRequest %s\n' "$i"
  curl -i --connect-timeout 5 --max-time 15 \
    https://app.teamcn.test:8443/api/status
done
```

### Observed Result

All six requests returned:

```text
HTTP/1.1 200 OK
X-Backend: B
```

### Layer Affected

Backend A's application service was unavailable. nginx's configured upstream retry and passive failure handling allowed requests to be served by Backend B.

### Restoration — Nitin

From the backend directory:

```bash
python3 server.py --backend A --port 3001
```

The subsequent six-request test returned HTTP 200 for every request with this sequence:

```text
B, B, A, B, A, B
```

This confirmed that Backend A was serving requests again.

## 6. Both Backends Stopped

### Before

The HTTPS service returned responses through nginx with both backends available.

### Fault Introduced

Nitin and Piyush stopped their backend processes.

### Client Test — Kartik

```bash
dig app.teamcn.test A +time=3 +tries=1

curl -v --connect-timeout 5 --max-time 15 \
  https://app.teamcn.test:8443/api/status
```

### Observed Result

- DNS returned the correct edge IP.
- The TLS handshake succeeded.
- Curl reported `SSL certificate verify ok.`
- nginx returned `HTTP/1.1 502 Bad Gateway`.

### Layer Affected

The upstream application services were unavailable. The client could still resolve the domain and establish HTTPS with nginx, but nginx could not obtain a response from either backend.

### Restoration

Nitin restarted Backend A:

```bash
python3 server.py --backend A --port 3001
```

Piyush restarted Backend B:

```bash
python3 server.py --backend B --port 3002
```

Kartik repeated the six-request test. All requests returned HTTP 200, with backend sequence:

```text
B, B, A, B, A, B
```

## 7. Wrong Destination Port

### Before

The HTTPS service used port `8443`.

### Fault Introduced — Piyush

Piyush intentionally requested port `8444`:

```bash
dig app.teamcn.test A +time=3 +tries=1

curl -v --connect-timeout 5 --max-time 10 \
  https://app.teamcn.test:8444/api/status
```

### Observed Result

DNS resolved correctly to `10.63.169.72`, but the TCP connection to port `8444` was refused.

Curl reported:

```text
curl: (7) Failed to connect to app.teamcn.test port 8444
```

### Layer Affected

The failure occurred during transport-layer connection establishment. The correct host was targeted, but the selected destination port had no listening service.

The TLS handshake did not begin.

### Restoration — Piyush

```bash
curl -i --connect-timeout 5 --max-time 15 \
  https://app.teamcn.test:8443/api/status
```

Recorded result:

```text
HTTP/1.1 200 OK
X-Backend: B
```

## 8. Final Restored State

After the demonstrations:

- Both project DNS records pointed to `10.63.169.72`.
- The private DNS server was running.
- nginx HTTPS was available on port `8443`.
- Responses from both backends had been verified.
- The final recorded DNS recovery test returned the correct edge IP and HTTP 200 from Backend A.

## 9. Failure Demonstration Video

The form-selected scenario is **Wrong Client DNS**.

The video should show:

1. Successful private DNS resolution
2. Client DNS changed to `8.8.8.8`
3. NXDOMAIN with successful IP ping
4. Private DNS restored to `10.63.169.3`
5. Successful domain resolution again

Include an explanation of the affected layer and recovery. A screenshot slideshow should be identified as recorded evidence rather than a live command demonstration.

## 10. Supporting Evidence

- [Wrong Client DNS](../evidence/28_wrong_client_dns_failure.md)
- [Wrong Destination Port](../evidence/29_wrong_port_failure.md)
- [Backend A Stopped](../evidence/30_single_backend_failover.md)
- [Both Backends Stopped](../evidence/31_both_backends_down.md)
- [Wrong Record Setup](../evidence/32_wrong_record_setup.md)
- [Wrong Record Failure and Recovery](../evidence/33_wrong_record_failure.md)

Perform one fault at a time and restore the working state before the next test. The wrong-record DNS configuration is a demonstration file, not the normal working configuration.
