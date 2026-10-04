# Phase 1 — Default Client DNS Verification

## 1. Evidence Source

Terminal outputs and original screenshots were supplied on **2026-10-03** for Kartik and Piyush.

The screenshots show configured Wi-Fi DNS settings, ordinary `dig` queries without an explicit `@server` argument, and macOS hostname lookup results.

## 2. Configure Client DNS

Both clients executed:

```bash
sudo networksetup -setdnsservers "Wi-Fi" 10.63.169.3
```

They then checked the configured DNS server:

```bash
networksetup -getdnsservers "Wi-Fi"
```

Recorded output on both clients:

```text
10.63.169.3
```

## 3. Default DNS Query Commands

Both clients ran:

```bash
dig app.teamcn.test A
```

```bash
dig api.teamcn.test A
```

These commands do not specify an explicit DNS server. The recorded responses identify **10.63.169.3#53** as the server used.

## 4. Recorded Query Results

Execution times are recorded in **IST**.

| Client | Query | Execution Time (IST) | Query Time (ms) | Query ID |
|---|---|---|---:|---:|
| Kartik | app.teamcn.test A | 2026-10-03 19:40:16 | 56 | 59756 |
| Kartik | api.teamcn.test A | 2026-10-03 19:40:34 | 18 | 23566 |
| Piyush | app.teamcn.test A | 2026-10-03 19:39:55 | 14 | 65073 |
| Piyush | api.teamcn.test A | 2026-10-03 19:40:03 | 11 | 3165 |

All four queries returned:

| Field | Recorded Value |
|---|---|
| Status | NOERROR |
| Answer type | A |
| Returned IPv4 address | 10.63.169.72 |
| TTL | 60 seconds |
| DNS server | 10.63.169.3#53 |

Both project names resolved to Kartik's nginx host.

## 5. macOS Hostname Lookup

Both clients also ran:

```bash
dscacheutil -q host -a name app.teamcn.test
```

Both recorded outputs included:

```text
name: app.teamcn.test
ip_address: 10.63.169.72
```

This verifies that the macOS hostname lookup returned the expected project address.

## 6. Original Screenshot Evidence

### Kartik — Configured DNS and Lookup Results

![Kartik default DNS verification](Kartik_default_DNS.png)

### Piyush — Configured DNS and Lookup Results

![Piyush default DNS verification](Piyush_default_DNS.jpg)

## 7. Interpretation

Kartik and Piyush configured their Wi-Fi DNS to use Nitin's resolver at **10.63.169.3**.

Their ordinary app/api queries returned the expected address, and the `SERVER` fields identify Nitin's resolver. The macOS lookup results also returned **10.63.169.72**.

Together with the earlier explicit queries, these results verify the private DNS setup on two client Macs.

## 8. Subsequent HTTPS Verification

Trusted HTTPS access through the project domain was subsequently verified separately.

DNS lookup establishes the destination address; TCP connectivity, TLS certificate validation and HTTP responses require their own evidence.

See [HTTPS System Trust Verification](23_https_system_trust_verified.md).

## 9. Related Documents

- [Explicit Client DNS Queries](11_explicit_dns_queries.md)
- [Original DNS Settings and Forwarding](12_original_dns_and_forwarding.md)
- [DNS Setup Instructions](../configs/DNS_Setup.md)
- [DNS Rollback Instructions](../configs/DNS_Rollback.md)
- [HTTPS System Trust Verification](23_https_system_trust_verified.md)
- [DNS Packet Analysis](27_packet_analysis_verified.md)
