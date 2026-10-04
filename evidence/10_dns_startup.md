# Phase 1 — DNS Validation and Startup Evidence

## 1. Evidence Source

This document records Nitin's terminal outputs supplied on **2026-10-03**. Exact command execution timestamps were not supplied.

The startup log excerpt is transcribed from supplied output. Original startup screenshots are not linked here.

## 2. DNS Server Details

| Item | Value |
|---|---|
| Server owner | Nitin Kumar |
| Project IPv4 address | 10.63.169.3 |
| Software | dnsmasq 2.93 |
| DNS port | UDP/TCP 53 |
| Local project zone | teamcn.test |
| Configured upstream resolver | 10.63.169.210 |
| Project record destination | 10.63.169.72 |

Configuration file on Nitin's Mac:

```text
~/Documents/CN_Phase1/configs/dnsmasq-phase1.conf
```

Repository configuration: [dnsmasq-phase1.conf](../configs/dnsmasq-phase1.conf).

## 3. Configuration Validation

### Command

```bash
/opt/homebrew/opt/dnsmasq/sbin/dnsmasq \
  --test \
  --conf-file="$HOME/Documents/CN_Phase1/configs/dnsmasq-phase1.conf"
```

### Recorded Output

```text
dnsmasq: syntax check OK.
```

The configuration passed dnsmasq's syntax check.

## 4. DNS Startup

After successful validation, Nitin started dnsmasq in a dedicated terminal.

### Command

```bash
sudo /opt/homebrew/opt/dnsmasq/sbin/dnsmasq \
  --keep-in-foreground \
  --conf-file="$HOME/Documents/CN_Phase1/configs/dnsmasq-phase1.conf"
```

### Recorded Startup Log Excerpt

```text
dnsmasq[63944]: started, version 2.93 cachesize 150
dnsmasq[63944]: using nameserver 10.63.169.210#53
dnsmasq[63944]: using only locally-known addresses for teamcn.test
dnsmasq[63944]: cleared cache
```

The PID `63944` belongs to this recorded startup session. It must not be treated as the current process ID during a later demonstration.

## 5. Interpretation

The startup log confirms that dnsmasq started successfully, selected **10.63.169.210:53** as its upstream resolver and treated **teamcn.test** as a local zone.

The working configuration defines:

| DNS Name | IPv4 Answer |
|---|---|
| app.teamcn.test | 10.63.169.72 |
| api.teamcn.test | 10.63.169.72 |

Startup logs alone do not prove that clients can query the server or that external forwarding succeeds.

## 6. Subsequent Client Verification

Later recorded tests verified:

- Explicit app/api DNS queries from Kartik and Piyush.
- Correct answers pointing to **10.63.169.72**.
- System DNS configuration and default lookups on both clients.
- External DNS forwarding through Nitin's resolver.
- A project DNS query and response in the saved Wireshark capture.

These results are documented separately below. The recorded Wireshark DNS exchange used UDP; this file does not claim a separate DNS-over-TCP test.

## 7. Setup Note

During setup, the syntax-check output was accidentally entered as a shell command, producing:

```text
zsh: command not found: dnsmasq:
```

This was a shell input error and did not invalidate the successful configuration check or subsequent DNS startup.

## 8. Related Evidence

- [DNS Prerequisites](09_dns_prerequisites.md)
- [Explicit DNS Queries](11_explicit_dns_queries.md)
- [Original DNS Settings and Forwarding](12_original_dns_and_forwarding.md)
- [Default Client DNS Verification](13_default_dns_verified.md)
- [Verified Packet Analysis](27_packet_analysis_verified.md)
- [DNS Setup Instructions](../configs/DNS_Setup.md)
- [Client DNS Rollback Instructions](../configs/DNS_Rollback.md)
