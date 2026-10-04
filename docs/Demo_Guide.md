# Phase 1 Live Demonstration Guide

This guide assigns each demonstration step to Nitin, Kartik and Piyush.

The recorded setup uses three Macs on Kartik's phone hotspot. Keep all server terminals open during the demonstration.

## 1. Member Responsibilities

| Member | Responsibilities |
|---|---|
| Nitin | Private DNS, Backend A, architecture explanation |
| Kartik | nginx, TLS configuration, load balancing explanation |
| Piyush | Backend B, client tests, caching and Wireshark |

## 2. Check the Network First

Run on all three Macs:

```bash
ipconfig getifaddr en0
route -n get default
```

Recorded addresses:

| Machine | IP |
|---|---|
| Nitin | 10.63.169.3 |
| Kartik | 10.63.169.72 |
| Piyush | 10.63.169.63 |

If addresses have changed, update DNS listener and records, nginx upstream addresses and client DNS settings before continuing.

Use the existing certificate and matching private key. Do not regenerate the certificate merely to restart the services.

## 3. Start the Services

Start only services that are currently stopped.

### Nitin — Backend A

In one terminal:

```bash
cd ~/Documents/CN_Phase1/backend
python3 server.py --backend A --port 3001
```

### Nitin — Private DNS

In a separate terminal, validate:

```bash
/opt/homebrew/opt/dnsmasq/sbin/dnsmasq \
  --test \
  --conf-file="$HOME/Documents/CN_Phase1/configs/dnsmasq-phase1.conf"
```

After successful validation, start:

```bash
sudo /opt/homebrew/opt/dnsmasq/sbin/dnsmasq \
  --keep-in-foreground \
  --conf-file="$HOME/Documents/CN_Phase1/configs/dnsmasq-phase1.conf"
```

### Piyush — Backend B

```bash
cd ~/Documents/CN_Phase1/backend
python3 server.py --backend B --port 3002
```

### Kartik — nginx

Validate the existing HTTPS configuration:

```bash
nginx -t \
  -p "$HOME/Documents/CN_Phase1/edge/" \
  -c nginx.conf
```

After successful validation, start:

```bash
nginx \
  -p "$HOME/Documents/CN_Phase1/edge/" \
  -c nginx.conf \
  -g 'daemon off;'
```

Keep these four service terminals open. Use separate terminals for client commands.

## 4. Configure Client DNS

Kartik and Piyush each run:

```bash
sudo networksetup -setdnsservers "Wi-Fi" 10.63.169.3
networksetup -getdnsservers "Wi-Fi"
```

The certificate was already trusted on all three Macs during setup. If using a new Mac, follow [Client Certificate Trust](../configs/TLS_Client_Trust.md).

## 5. Present the Architecture — Nitin

Open [Architecture](Architecture.md) and explain:

- Three Macs with combined roles
- Private DNS points both domains to nginx
- Client HTTPS terminates at nginx
- nginx forwards HTTP to Backend A or Backend B
- X-Backend identifies the selected backend

## 6. Demonstrate LAN Connectivity — All Members

Each member pings the other two Macs.

### Nitin

```bash
ping -c 4 10.63.169.72
ping -c 4 10.63.169.63
```

### Kartik

```bash
ping -c 4 10.63.169.3
ping -c 4 10.63.169.63
```

### Piyush

```bash
ping -c 4 10.63.169.3
ping -c 4 10.63.169.72
```

The recorded tests received four replies with zero loss in every direction.

## 7. Demonstrate Private DNS — Kartik and Piyush

Run on both clients:

```bash
dig app.teamcn.test A
dig api.teamcn.test A
dscacheutil -q host -a name app.teamcn.test
```

Show:

- NOERROR status
- Answer IP 10.63.169.72
- DNS SERVER line 10.63.169.3#53

To compare with public DNS:

```bash
dig @8.8.8.8 app.teamcn.test A +time=3 +tries=1
```

The recorded public DNS test returned NXDOMAIN.

## 8. Demonstrate Trusted HTTPS — Piyush

```bash
curl -v --connect-timeout 5 --max-time 15 \
  https://app.teamcn.test:8443/api/status
```

Show:

- TLS negotiation
- Certificate hostname match
- SSL certificate verify ok.
- HTTP 200
- X-Backend header

Kartik explains certificate trust and TLS termination.

## 9. Demonstrate Load Balancing — Piyush

```bash
for i in 1 2 3 4 5 6; do
  printf '\nRequest %s\n' "$i"
  curl -i --connect-timeout 5 --max-time 15 \
    https://app.teamcn.test:8443/api/status
done
```

Show successful responses from both backends.

nginx uses default round-robin balancing. Preserve the actual output sequence; do not claim every recorded run strictly alternated.

## 10. Demonstrate HTTP Caching — Piyush

Follow [Caching Test](05_Caching_Test.md).

Show:

1. HTTP 200 with the response body
2. Cache-Control: public, max-age=60
3. The ETag value
4. A request using If-None-Match
5. HTTP 304 without a response body

Explain that this is explicit conditional validation. Curl does not automatically maintain a browser-style response cache.

## 11. Present Wireshark Evidence — Piyush and Nitin

Open the saved capture:

```text
evidence/Phase1_DNS_TCP_TLS.pcapng
```

### DNS Filter

```text
dns.qry.name == "app.teamcn.test"
```

Explain frames 15 and 16:

- Client: 10.63.169.63:65089
- DNS server: 10.63.169.3:53
- Returned edge IP: 10.63.169.72
- TTL: 60 seconds

### TCP Filter

```text
frame.number >= 21 && frame.number <= 23
```

Explain SYN, SYN-ACK and ACK:

- Client: 10.63.169.63:50050
- Server: 10.63.169.72:8443

### TLS Filter

```text
tls && tcp.port == 8443
```

Explain:

- Frame 24: Client Hello
- Frame 27: Server Hello and Certificate
- Frames 29 and 31: key exchange and cipher-state transition
- Frames 33 and 35: encrypted Application Data

The saved demonstration selected TLS 1.2. Ordinary HTTPS tests negotiated TLS 1.3.

New captures may have different frame numbers and ephemeral ports.

See [Packet Capture](06_Packet_Capture.md).

## 12. Demonstrate Failure and Recovery

Follow [Failure Demonstrations](07_Failure_Demonstrations.md). Perform one fault at a time and restore it before introducing another.

| Scenario | Action Owner | Test Owner |
|---|---|---|
| Wrong client DNS | Piyush | Piyush |
| Wrong DNS record | Nitin | Piyush |
| Backend A stopped | Nitin | Piyush |
| Both backends stopped | Nitin and Piyush | Kartik |
| Wrong destination port | Piyush | Piyush |

For the form-selected wrong-client-DNS scenario, show:

1. Working private DNS resolution
2. Client DNS changed to 8.8.8.8
3. NXDOMAIN while edge IP ping still works
4. Client DNS restored to 10.63.169.3
5. Correct domain resolution again

Explain the affected layer and confirm recovery.

## 13. Final Working-State Check

After the failure demonstrations, Piyush runs:

```bash
dig app.teamcn.test A

curl -i --connect-timeout 5 --max-time 15 \
  https://app.teamcn.test:8443/api/status
```

Confirm the correct DNS answer and HTTP 200. Repeat the load-balancing loop to confirm that both backends are available.

## 14. Stop Services After the Demonstration

### Backends — Nitin and Piyush

Press Ctrl+C in each backend's own terminal.

### nginx — Kartik

```bash
nginx \
  -p "$HOME/Documents/CN_Phase1/edge/" \
  -c nginx.conf \
  -s quit
```

### dnsmasq — Nitin

If Ctrl+C does not stop dnsmasq, identify the current process:

```bash
pgrep -fl dnsmasq
```

Verify the project process before stopping it:

```bash
ps -p <PID> -o pid=,comm=,args=
sudo kill -TERM <PID>
```

Replace `<PID>` with the verified current process ID. Never reuse an old recorded PID.

### Restore Client DNS

Kartik and Piyush restore their original settings using:

[DNS Rollback](../configs/DNS_Rollback.md)

## 15. Viva Preparation

Each member should understand DNS resolution, TCP connection establishment, TLS verification, reverse proxying, load balancing, conditional caching and failure recovery.

See [Viva Notes](Viva_Notes.md).

This guide covers Phase 1.
