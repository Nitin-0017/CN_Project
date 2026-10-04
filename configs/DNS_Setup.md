# Phase 1 DNS Setup

Chosen project zone: teamcn.test. Records app.teamcn.test and api.teamcn.test point to Kartik nginx edge 10.63.169.72. Nitin serves DNS on 10.63.169.3 port 53. Replace all addresses if DHCP changes.

Copy dnsmasq-phase1.conf to ~/Documents/CN_Phase1/configs/ on Nitin. Project configuration is independent of the Homebrew default configuration. No DHCP service is configured.

Validate:

```sh
/opt/homebrew/opt/dnsmasq/sbin/dnsmasq --test --conf-file="$HOME/Documents/CN_Phase1/configs/dnsmasq-phase1.conf"
```

Start in a dedicated terminal:

```sh
sudo /opt/homebrew/opt/dnsmasq/sbin/dnsmasq --keep-in-foreground --conf-file="$HOME/Documents/CN_Phase1/configs/dnsmasq-phase1.conf"
```

Keep it running; Ctrl C stops it. Allow incoming connections if macOS asks. Forwarding for nonproject names is configured to the current hotspot gateway 10.63.169.210; its recursive DNS capability is unverified and must be checked before changing client DNS settings. Project zone stays local.

Initial client test on Kartik and Piyush (does not change system settings):

```sh
dig @10.63.169.3 app.teamcn.test A
dig @10.63.169.3 api.teamcn.test A
```

Expected: NOERROR, A 10.63.169.72, SERVER 10.63.169.3#53. System DNS configuration on both clients remains a separate required step. Capture those original settings before modifying them for rollback. Nitin supplied successful syntax-check and foreground startup logs. Explicit app/api dig tests passed on both Kartik and Piyush. System resolver configuration, default app/api queries, macOS lookup and external forwarding passed on both clients.

References: https://thekelleys.org.uk/dnsmasq/docs/dnsmasq-man.html

## Configure client DNS

External forwarding through Nitin passed on both clients. Original settings and restore commands are recorded in DNS_Rollback.md.

Kartik and Piyush each run:

```sh
sudo networksetup -setdnsservers "Wi-Fi" 10.63.169.3
networksetup -getdnsservers "Wi-Fi"
dig app.teamcn.test A
dig api.teamcn.test A
dscacheutil -q host -a name app.teamcn.test
```

Expect configured DNS 10.63.169.3, dig SERVER 10.63.169.3#53, NOERROR and A 10.63.169.72, plus system resolver output ip_address 10.63.169.72. This step passed on both clients, with original screenshots in evidence/.
