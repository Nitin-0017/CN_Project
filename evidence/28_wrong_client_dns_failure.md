# Phase 1 — Wrong Client DNS Failure and Recovery

## 1. Evidence Source

This demonstration was performed by **Piyush** on **2026-10-03**.

The recorded results are supported by supplied terminal outputs and these original screenshots:

- Piyush_default_DNS.jpg
- Piyush_failure_wrong_DNS.jpg
- Piyush_restore_DNS.jpg

## 2. Before State — Working Project DNS

Piyush's Wi-Fi DNS was configured to use Nitin's resolver:

```text
10.63.169.3
```

Ordinary queries for `app.teamcn.test` returned:

```text
app.teamcn.test. 60 IN A 10.63.169.72
```

The earlier working state is documented in [Default Client DNS Verification](13_default_dns_verified.md).

### Before Screenshot

![Piyush working project DNS](Piyush_default_DNS.jpg)

## 3. Fault Introduced

Piyush changed his Wi-Fi DNS server to Google's public resolver:

```bash
sudo networksetup -setdnsservers "Wi-Fi" 8.8.8.8
```

He checked the setting:

```bash
networksetup -getdnsservers "Wi-Fi"
```

Recorded output:

```text
8.8.8.8
```

Nitin's project DNS service remained running throughout the demonstration.

## 4. After State — DNS Lookup Failure

Piyush ran:

```bash
dig app.teamcn.test A +time=3 +tries=1
```

### Recorded Result

| Field | Value |
|---|---|
| Execution time (IST) | 2026-10-03 20:47:10 |
| Status | NXDOMAIN |
| Answer count | 0 |
| DNS server | 8.8.8.8#53 |
| Query time | 42 ms |
| Query ID | 27058 |

The public resolver did not resolve the project's private hostname.

## 5. Direct IP Connectivity Check

Piyush also ran:

```bash
ping -c 4 10.63.169.72
```

### Recorded Result

| Field | Value |
|---|---|
| Packets sent | 4 |
| Replies received | 4 |
| Packet loss | 0.0% |
| RTT min/avg/max/stddev | 10.011 / 51.730 / 87.545 / 28.438 ms |

The successful ping demonstrates that Kartik's host remained reachable by IP during the DNS failure. It does not independently verify HTTPS service availability.

### Failure Screenshot

![Wrong client DNS and successful direct IP ping](Piyush_failure_wrong_DNS.jpg)

## 6. Layer Affected

The fault affected **DNS name resolution at the application layer**.

The client queried a public resolver that did not have the project's private DNS record, so the hostname lookup returned NXDOMAIN.

Direct IP ping still worked, showing that IP reachability remained available during this test.

## 7. Restore the Working Project DNS

Piyush restored Nitin's resolver:

```bash
sudo networksetup -setdnsservers "Wi-Fi" 10.63.169.3
```

He then checked the setting and repeated the lookup:

```bash
networksetup -getdnsservers "Wi-Fi"
dig app.teamcn.test A +time=3 +tries=1
```

### Recorded Restoration Result

| Field | Value |
|---|---|
| Verification time (IST) | 2026-10-03 20:48:14 |
| Configured DNS server | 10.63.169.3 |
| Query status | NOERROR |
| Answer count | 1 |
| A answer | 10.63.169.72 |
| TTL | 60 seconds |
| Response server | 10.63.169.3#53 |
| Query time | 13 ms |
| Query ID | 18704 |

### Restoration Screenshot

![Piyush restored project DNS and successful lookup](Piyush_restore_DNS.jpg)

## 8. Outcome

The demonstration recorded:

```text
Before: Project hostname resolves through 10.63.169.3
Fault: Client DNS changed to 8.8.8.8
After: NXDOMAIN, while direct IP ping succeeds
Recovery: DNS restored to 10.63.169.3 and correct answer returned
```

The failure and restoration were verified.

Restoring the working project DNS is distinct from restoring the client's original pre-project DNS settings after the entire demonstration.

## 9. Related Documents

- [Default Client DNS Verification](13_default_dns_verified.md)
- [Original Client DNS Settings](12_original_dns_and_forwarding.md)
- [Client DNS Rollback Instructions](../configs/DNS_Rollback.md)
- [Failure Demonstration Results](../docs/07_Failure_Demonstrations.md)
