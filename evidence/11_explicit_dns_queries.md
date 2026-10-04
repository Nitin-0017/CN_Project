# Phase 1 — Explicit Client DNS Query Evidence

## 1. Evidence Source

This document summarizes supplied `dig` outputs from Kartik and Piyush, recorded on **2026-10-03**.

Both clients explicitly queried Nitin's DNS server at **10.63.169.3**.

The results below are terminal transcriptions. Original screenshots of these four explicit queries are not linked here.

## 2. Commands Used

Both clients ran:

```bash
dig @10.63.169.3 app.teamcn.test A
```

```bash
dig @10.63.169.3 api.teamcn.test A
```

The `@10.63.169.3` argument explicitly selects the DNS server for each query.

## 3. Common Response Details

All four supplied outputs recorded:

| Field | Recorded Value |
|---|---|
| Client tool | DiG 9.10.6 |
| DNS server | 10.63.169.3#53 |
| Response status | NOERROR |
| Flags | qr aa rd ra |
| Answer count | 1 |
| Answer type | A |
| Returned IPv4 address | 10.63.169.72 |
| Answer TTL | 60 seconds |
| Received message size | 60 bytes |

## 4. Recorded Query Results

Execution times are shown in **IST**, as recorded in the supplied outputs.

| Client | Queried Name | A Answer | Query Time (ms) | Execution Time (IST) | Query ID |
|---|---|---|---:|---|---:|
| Piyush | app.teamcn.test | 10.63.169.72 | 884 | 2026-10-03 19:33:47 | 18142 |
| Piyush | api.teamcn.test | 10.63.169.72 | 29 | 2026-10-03 19:33:59 | 2097 |
| Kartik | app.teamcn.test | 10.63.169.72 | 3482 | 2026-10-03 19:33:47 | 21403 |
| Kartik | api.teamcn.test | 10.63.169.72 | 96 | 2026-10-03 19:34:06 | 51963 |

## 5. Recorded Answer Records

For `app.teamcn.test`:

```text
app.teamcn.test.  60  IN  A  10.63.169.72
```

For `api.teamcn.test`:

```text
api.teamcn.test.  60  IN  A  10.63.169.72
```

Both names resolve to Kartik's nginx host.

## 6. Interpretation

All four queries returned **NOERROR** with the expected IPv4 address. This verifies that both clients could query Nitin's DNS server and receive the correct project records at the time of testing.

The TTL of **60 seconds** specifies how long the DNS answer may be cached before it expires.

Query times varied between requests. These outputs do not establish the cause of that variation.

## 7. Scope and Subsequent Verification

These commands explicitly select Nitin's resolver. They do not, by themselves, prove that either client's default system DNS settings use that resolver.

Default client DNS configuration and ordinary lookups were subsequently verified separately. Original DNS settings and external forwarding results are also recorded in the linked documents below.

## 8. Related Evidence

- [DNS Validation and Startup](10_dns_startup.md)
- [Original DNS Settings and External Forwarding](12_original_dns_and_forwarding.md)
- [Default Client DNS Verification](13_default_dns_verified.md)
- [DNS Packet Analysis](27_packet_analysis_verified.md)
- [Working DNS Configuration](../configs/dnsmasq-phase1.conf)
- [DNS Setup Instructions](../configs/DNS_Setup.md)
