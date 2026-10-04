# DNS Validation and Startup Evidence

Source: Nitin terminal output supplied by user, received 2026-10-03. Exact execution timestamps not supplied.

Config: ~/Documents/CN_Phase1/configs/dnsmasq-phase1.conf, matching configs/dnsmasq-phase1.conf in this bundle.

Validation command:

```sh
/opt/homebrew/opt/dnsmasq/sbin/dnsmasq --test --conf-file="$HOME/Documents/CN_Phase1/configs/dnsmasq-phase1.conf"
```

Result: dnsmasq: syntax check OK.

The user then pasted the result text as a shell command, yielding zsh: command not found: dnsmasq:. This did not prevent the subsequent successful start.

Startup command:

```sh
sudo /opt/homebrew/opt/dnsmasq/sbin/dnsmasq --keep-in-foreground --conf-file="$HOME/Documents/CN_Phase1/configs/dnsmasq-phase1.conf"
```

Observed log excerpt:

```text
dnsmasq[63944]: started, version 2.93 cachesize 150
dnsmasq[63944]: using nameserver 10.63.169.210#53
dnsmasq[63944]: using only locally-known addresses for teamcn.test
dnsmasq[63944]: cleared cache
```

DNS process started; remote queries, TCP DNS and system client resolver configuration are not yet verified. Upstream nameserver configuration is reported but successful external forwarding is not yet proven. Original screenshot not supplied.
