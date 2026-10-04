# Phase 1 Private DNS Setup

Nitin's Mac runs dnsmasq as the private DNS server. The project domains resolve to Kartik's nginx edge server.

## 1. Network and DNS Records

| Item | Recorded Value |
|---|---|
| Private DNS server | Nitin — 10.63.169.3 |
| DNS port | 53 |
| nginx edge server | Kartik — 10.63.169.72 |
| Client machines | Kartik and Piyush |
| Network interface | en0 |
| Hotspot gateway | 10.63.169.210 |
| Project zone | teamcn.test |

| Domain | A Record |
|---|---|
| app.teamcn.test | 10.63.169.72 |
| api.teamcn.test | 10.63.169.72 |

These addresses were used during the recorded demonstration. Recheck the IP addresses after reconnecting to the hotspot.

## 2. Install dnsmasq — Nitin

Run on Nitin's Mac if dnsmasq is not already installed:

```bash
brew install dnsmasq
```

The recorded installation used dnsmasq 2.93 under `/opt/homebrew`.

## 3. Project Configuration

Configuration file on Nitin's Mac:

```text
~/Documents/CN_Phase1/configs/dnsmasq-phase1.conf
```

Actual tested configuration:

```conf
port=53
listen-address=127.0.0.1,10.63.169.3
bind-interfaces
no-hosts
no-resolv
server=10.63.169.210
local=/teamcn.test/
host-record=app.teamcn.test,10.63.169.72
host-record=api.teamcn.test,10.63.169.72
local-ttl=60
log-queries
log-facility=-
```

### Configuration Behaviour

- DNS listens on localhost and Nitin's LAN IP.
- The LAN listening address allows other Macs to query the server.
- Both project records point to the nginx edge.
- Project DNS answers use a TTL of 60 seconds.
- Queries within `teamcn.test` are handled locally.
- Other names are forwarded to the hotspot gateway.
- Query logs are displayed in the terminal.
- No DHCP service is configured.

The configuration uses `host-record` directives for the two project records.

## 4. Validate the Configuration — Nitin

```bash
/opt/homebrew/opt/dnsmasq/sbin/dnsmasq \
  --test \
  --conf-file="$HOME/Documents/CN_Phase1/configs/dnsmasq-phase1.conf"
```

Recorded output:

```text
dnsmasq: syntax check OK.
```

## 5. Start the DNS Server — Nitin

Run in a dedicated terminal:

```bash
sudo /opt/homebrew/opt/dnsmasq/sbin/dnsmasq \
  --keep-in-foreground \
  --conf-file="$HOME/Documents/CN_Phase1/configs/dnsmasq-phase1.conf"
```

Recorded startup logs confirmed:

```text
started, version 2.93 cachesize 150
using nameserver 10.63.169.210#53
using only locally-known addresses for teamcn.test
cleared cache
```

Keep this terminal open while clients use the project DNS.

## 6. Test DNS Directly — Kartik and Piyush

Run on each client:

```bash
dig @10.63.169.3 app.teamcn.test A
dig @10.63.169.3 api.teamcn.test A
```

Both clients successfully received:

- Status: `NOERROR`
- A-record answer: `10.63.169.72`
- DNS server: `10.63.169.3#53`

These commands query Nitin directly without changing the client's system DNS settings.

## 7. Verify External Forwarding

Run on each client:

```bash
dig @10.63.169.3 example.com A +time=3 +tries=1
```

Both clients received successful responses with status `NOERROR`. This verified forwarding of non-project queries through Nitin's dnsmasq.

## 8. Configure Client DNS — Kartik and Piyush

Original DNS settings were recorded before making changes.

Run on both client Macs:

```bash
sudo networksetup -setdnsservers "Wi-Fi" 10.63.169.3
networksetup -getdnsservers "Wi-Fi"
```

Recorded result:

```text
10.63.169.3
```

### Test the Default Resolver

```bash
dig app.teamcn.test A
dig api.teamcn.test A
dscacheutil -q host -a name app.teamcn.test
```

Both clients resolved the project domains to `10.63.169.72`. The dig SERVER line showed `10.63.169.3#53`, and the macOS host lookup returned the same edge IP.

### Kartik Screenshot

![Kartik default DNS and successful project domain resolution](../evidence/Kartik_default_DNS.png)

### Piyush Screenshot

![Piyush default DNS and successful project domain resolution](../evidence/Piyush_default_DNS.jpg)

## 9. DNS Packet Capture Evidence

Piyush captured the DNS query and response using Wireshark on `en0`.

- Frame 15: A query for `app.teamcn.test` from `10.63.169.63:65089` to `10.63.169.3:53` over UDP.
- Frame 16: Matching response containing the A record `10.63.169.72`.
- Transaction ID: `0x9a52`.
- Answer TTL: 60 seconds.
- Query-response time: 13.587 milliseconds.

![Wireshark private DNS query and response](../evidence/Piyush_Wireshark_DNS.jpg)

See [Packet Capture Documentation](../docs/06_Packet_Capture.md) for DNS, TCP and TLS analysis.

## 10. Wrong Client DNS Failure Test

Piyush temporarily changed the client DNS to `8.8.8.8`.

The project domain returned `NXDOMAIN`, while pinging the edge IP still succeeded with zero packet loss. This demonstrated a DNS name-resolution failure while IP connectivity remained available.

![Wrong client DNS produces NXDOMAIN while IP ping succeeds](../evidence/Piyush_failure_wrong_DNS.jpg)

After restoring the client DNS to `10.63.169.3`, the domain resolved successfully again.

![Project DNS restored successfully](../evidence/Piyush_restore_DNS.jpg)

## 11. Stop dnsmasq

In the recorded session, Ctrl+C did not stop dnsmasq. It was stopped using SIGTERM after checking the process.

Find the current process:

```bash
pgrep -fl dnsmasq
```

Confirm that the process uses the project configuration:

```bash
ps -p <PID> -o pid=,comm=,args=
```

Stop the confirmed project process:

```bash
sudo kill -TERM <PID>
```

Replace `<PID>` with the current process ID. Do not reuse a process ID from an earlier session.

The recorded shutdown log reported:

```text
exiting on receipt of SIGTERM
```

## 12. Restore Original Client Settings

After the demonstration, restore the clients' original DNS settings using:

[DNS Rollback Instructions](DNS_Rollback.md)

## 13. Supporting Evidence

- [DNS Startup](../evidence/10_dns_startup.md)
- [Explicit DNS Queries](../evidence/11_explicit_dns_queries.md)
- [Original Settings and External Forwarding](../evidence/12_original_dns_and_forwarding.md)
- [Default Client DNS Verification](../evidence/13_default_dns_verified.md)
- [Original Packet Capture](../evidence/Phase1_DNS_TCP_TLS.pcapng)
