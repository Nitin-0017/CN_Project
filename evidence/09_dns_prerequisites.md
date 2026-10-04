# Phase 1 — DNS Prerequisite Evidence

## 1. Evidence Source

This document summarizes terminal outputs supplied on **2026-10-03** from Nitin's Mac, which hosts the project's private DNS server.

Exact command execution timestamps were not supplied. The results are transcribed from supplied outputs.

## 2. Recorded Installation Details

| Item | Recorded Value |
|---|---|
| DNS server owner | Nitin Kumar |
| Project IPv4 address | 10.63.169.3 |
| DNS software | dnsmasq |
| Installed version | 2.93 |
| Homebrew prefix | /opt/homebrew |
| Installation directory | /opt/homebrew/Cellar/dnsmasq/2.93 |
| Project executable path | /opt/homebrew/opt/dnsmasq/sbin/dnsmasq |
| DNS service port | UDP/TCP 53 |

The supplied installation output confirmed that dnsmasq was installed successfully.

## 3. Homebrew Prefix Check

Command:

```bash
brew --prefix
```

Recorded output:

```text
/opt/homebrew
```

## 4. Initial DNS Port Check

Before starting the project DNS server, Nitin checked for existing listeners:

```bash
sudo lsof -nP -iUDP:53 -iTCP:53
```

### Recorded Observation

The supplied command output displayed no listener entries.

This indicates that the check found no visible UDP or TCP listeners on port **53** at that time. It does not establish the port's availability at a later time.

## 5. Installation Notice

The installation output included an unrelated Homebrew MongoDB tap-trust notice.

The notice did not prevent dnsmasq installation. No tap-trust changes were made for this project step.

## 6. Subsequent DNS Verification

After these prerequisite checks, the project DNS configuration was validated and dnsmasq was started.

Subsequent client tests verified that:

- Explicit queries to **10.63.169.3** resolved the project names.
- `app.teamcn.test` and `api.teamcn.test` returned **10.63.169.72**.
- Kartik and Piyush successfully used Nitin's DNS server through their configured system resolver settings.

The detailed startup and query results are recorded in the linked evidence below.

## 7. Related Evidence

- [DNS Validation and Startup](10_dns_startup.md)
- [Explicit DNS Queries](11_explicit_dns_queries.md)
- [Original DNS Settings and Forwarding](12_original_dns_and_forwarding.md)
- [Default Client DNS Verification](13_default_dns_verified.md)
- [DNS Setup Instructions](../configs/DNS_Setup.md)
- [Working dnsmasq Configuration](../configs/dnsmasq-phase1.conf)
