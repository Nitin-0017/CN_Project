# Phase 1 — Original Client DNS Settings and Forwarding Tests

## 1. Evidence Source

This document summarizes terminal outputs supplied on **2026-10-03**.

Original client DNS settings were recorded before configuring the clients to use Nitin's project DNS server. Forwarding test timestamps are recorded in IST.

The content below is transcribed terminal evidence.

## 2. Original Client DNS Settings

### Kartik Yadav

Recorded network services:

- Thunderbolt Bridge
- Wi-Fi

The Wi-Fi DNS settings check returned:

```text
There aren't any DNS Servers set on Wi-Fi.
```

This means there were no manually configured Wi-Fi DNS entries. Automatic network-supplied DNS settings remained applicable.

### Piyush Yadav

Recorded network services:

- Thunderbolt Bridge
- Wi-Fi
- iPhone USB

Original manual Wi-Fi DNS entries, in their recorded order:

```text
8.8.8.8
4.2.2.2
```

## 3. External DNS Forwarding Test

Before changing client DNS settings, both clients explicitly queried Nitin's resolver for an external name:

```bash
dig @10.63.169.3 example.com A +time=3 +tries=1
```

The explicit `@10.63.169.3` argument selects Nitin's resolver for this request without changing the client's system DNS settings.

## 4. Recorded Forwarding Results

Both clients received:

- **Status:** NOERROR
- **DNS server:** 10.63.169.3#53
- **A answers:** 172.66.147.243 and 104.20.23.154

| Client | Execution Time (IST) | Query Time (ms) | Recorded TTL (seconds) | Query ID |
|---|---|---:|---:|---:|
| Kartik | 2026-10-03 19:36:29 | 72 | 134 | 44220 |
| Piyush | 2026-10-03 19:36:39 | 24 | 124 | 58645 |

The returned addresses and TTLs are historical results from these tests.

## 5. Interpretation

Both clients successfully resolved an external name through Nitin's DNS server at the recorded test times. This provides evidence that external DNS forwarding worked through the project resolver.

These explicit queries do not, by themselves, verify either client's default DNS configuration.

Kartik and Piyush subsequently configured their Wi-Fi DNS to **10.63.169.3** and verified ordinary project-name lookups. Those results are recorded in [Default Client DNS Verification](13_default_dns_verified.md).

## 6. Restore Original Settings After the Demo

These commands restore the original settings recorded above. Run them after completing the project demonstration or when leaving the project network.

### Kartik — Restore Automatic DNS

```bash
sudo networksetup -setdnsservers "Wi-Fi" Empty
```

### Piyush — Restore Original Manual DNS Entries

```bash
sudo networksetup -setdnsservers "Wi-Fi" 8.8.8.8 4.2.2.2
```

### Verify Settings

On each client:

```bash
networksetup -getdnsservers "Wi-Fi"
```

During the working project demonstration, Kartik and Piyush use **10.63.169.3** as their configured DNS server. Restoring their original settings is a separate cleanup step.

## 7. Related Evidence

- [DNS Validation and Startup](10_dns_startup.md)
- [Explicit Project DNS Queries](11_explicit_dns_queries.md)
- [Default Client DNS Verification](13_default_dns_verified.md)
- [DNS Setup Instructions](../configs/DNS_Setup.md)
- [DNS Rollback Instructions](../configs/DNS_Rollback.md)
