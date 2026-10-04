# Phase 1 — Wrong DNS Record Failure and Recovery

## 1. Evidence Source

This document summarizes supplied terminal outputs from Nitin and Piyush on **2026-10-03**.

Nitin introduced and restored the DNS record fault. Piyush tested the resulting lookup, connection failure and recovery.

Original failure and recovery screenshots were not supplied. This document preserves transcribed terminal evidence.

## 2. Before State

The correct project DNS records point to Kartik's nginx host:

| DNS Name | Correct IPv4 Address |
|---|---|
| app.teamcn.test | 10.63.169.72 |
| api.teamcn.test | 10.63.169.72 |

The working HTTPS endpoint is:

```text
https://app.teamcn.test:8443/api/status
```

Earlier successful operation is documented in [HTTPS System Trust Verification](23_https_system_trust_verified.md).

## 3. Fault Introduced

Nitin changed the app record to the wrong destination:

```ini
host-record=app.teamcn.test,10.63.169.3
```

The api record remained pointed to **10.63.169.72**.

The fault setup is documented in [Wrong Record Fault Setup](32_wrong_record_setup.md).

## 4. Client Cache Clearing

Piyush cleared the macOS DNS cache before testing:

```bash
sudo dscacheutil -flushcache
sudo killall -HUP mDNSResponder
```

## 5. Recorded DNS Failure State

Piyush ran:

```bash
dig app.teamcn.test A
```

| Field | Recorded Value |
|---|---|
| Execution time (IST) | 2026-10-03 21:16:30 |
| Status | NOERROR |
| A answer | 10.63.169.3 — incorrect destination |
| TTL | 60 seconds |
| DNS server | 10.63.169.3#53 |
| Query time | 61 ms |
| Query ID | 64238 |

DNS returned an answer successfully, but the answer pointed to Nitin instead of the nginx host.

## 6. Recorded Connection Failure

Piyush's ordinary HTTPS curl request resolved the hostname to the incorrect address.

| Field | Recorded Value |
|---|---|
| Client endpoint | 10.63.169.63:50332 |
| Attempted destination | 10.63.169.3:8443 |
| Connection result | Connection refused |
| curl error | 7 |
| Reported elapsed time | Approximately 1079 ms |

The failure occurred before TLS negotiation and before an HTTP response.

## 7. Layer and Component Affected

The fault originated in the **application-layer DNS record configuration**.

The incorrect answer directed the client to the wrong host. The subsequent TCP connection to that host on port 8443 was refused.

Unlike the wrong-client-DNS test, this lookup returned **NOERROR** rather than NXDOMAIN. A successful DNS response status does not guarantee that the returned destination is correct.

## 8. Restore the Correct DNS Configuration

Nitin restored the original configuration backup.

The supplied restoration output confirmed both records:

```ini
host-record=app.teamcn.test,10.63.169.72
host-record=api.teamcn.test,10.63.169.72
```

The restored configuration passed the syntax check.

A new dnsmasq process, recorded as PID **21865**, started with:

- dnsmasq version 2.93
- Upstream resolver 10.63.169.210#53
- Local zone teamcn.test
- Cleared cache and active forwarding logs

PID 21865 belongs to this historical session and must not be reused as a current process ID.

## 9. Recorded Client Recovery

After restoration, Piyush cleared the client DNS cache again and repeated the lookup.

### DNS Recovery

| Field | Recorded Value |
|---|---|
| Execution time (IST) | 2026-10-03 21:21:22 |
| Status | NOERROR |
| A answer | 10.63.169.72 — correct nginx destination |
| TTL | 60 seconds |
| DNS server | 10.63.169.3#53 |
| Query time | 121 ms |
| Query ID | 41945 |

### HTTPS Recovery

The subsequent ordinary trusted HTTPS request returned:

| Field | Recorded Value |
|---|---|
| HTTP status | 200 OK |
| Backend identifier | A |
| Response Date (UTC) | 2026-10-03 15:51:29 |
| Equivalent time (IST) | 2026-10-03 21:21:29 |

The earlier wrong-IP curl output included in the supplied message belongs to the pre-recovery failure. The later correct lookup and HTTP 200 response establish recovery.

## 10. Outcome

```text
Before: app.teamcn.test points to 10.63.169.72
Fault: App record changed to 10.63.169.3
After: DNS returns the wrong IP; TCP 8443 connection is refused
Recovery: Correct record restored; DNS returns 10.63.169.72; HTTPS returns 200 from A
```

The wrong-record failure and service restoration were verified from supplied terminal outputs.

## 11. Related Evidence

- [Wrong Record Fault Setup](32_wrong_record_setup.md)
- [Working DNS Configuration](../configs/dnsmasq-phase1.conf)
- [Default Client DNS Verification](13_default_dns_verified.md)
- [HTTPS System Trust Verification](23_https_system_trust_verified.md)
- [Failure Demonstration Results](../docs/07_Failure_Demonstrations.md)
