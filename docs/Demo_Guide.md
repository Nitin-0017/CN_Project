# Phase 1 Named Live Demo Guide

Use the same Kartik hotspot. Keep Macs awake and power connected. Recheck IPs first; if addresses change, update DNS listener/records, nginx upstreams and client resolver settings before demonstration. Never reuse old PID values to stop a process; inspect current process identity.

## Start services

Nitin starts Backend A from ~/Documents/CN_Phase1/backend:

```sh
python3 server.py --backend A --port 3001
```

Nitin starts DNS in a separate tab:

```sh
sudo /opt/homebrew/opt/dnsmasq/sbin/dnsmasq --keep-in-foreground --conf-file="$HOME/Documents/CN_Phase1/configs/dnsmasq-phase1.conf"
```

Piyush starts Backend B from ~/Documents/CN_Phase1/backend:

```sh
python3 server.py --backend B --port 3002
```

Kartik validates then starts nginx in a dedicated tab if not already running:

```sh
nginx -t -p "$HOME/Documents/CN_Phase1/edge/" -c nginx.conf
nginx -p "$HOME/Documents/CN_Phase1/edge/" -c nginx.conf -g 'daemon off;'
```

Do not launch duplicate services. Server tabs stay running. Installed trusted public certificate is on all clients; private server.key stays locally on Kartik.

## Presentation sequence

1. Nitin shows Architecture.md: role map, hotspot, IP/service table and request flow. Explain combined roles for three members.
2. All show ping evidence; repeat live peer pings if asked.
3. Piyush and Kartik show DNS resolver10.63.169.3 and dig app.teamcn.test A, dig api.teamcn.test A without @. Nitin explains directory lookup versus subsequent connection.
4. Piyush runs curl -v https://app.teamcn.test:8443/api/status without -k/--cacert. Kartik explains TLS termination and domain/certificate validation.
5. Piyush runs six sequential curl -i HTTPS /api/status requests. Show both X-BackendA/B. Kartik explains round-robin and private upstream HTTP.
6. Nitin presents saved capture with Piyush: DNS15/16, TCP21-23, TLS24/27/29/31, encrypted data33/35. Explain client50050 vs server8443 and DNS source65089/server53. Real new captures will have different ports/frame numbers.
7. Piyush demonstrates caching using docs/05_Caching_Test.md:200+ETag then If-None-Match304. Explain fresh cache, validation and full response.
8. Demonstrate the five requested failures using docs/07_Failure_Demonstrations.md and the evidence folder; restore each before next. Live one-backend failover is particularly clear. Stop only backend tabs, never DNS by mistake.
9. All answer individual viva from understanding. Phase2 backupDNS/TTLcutover/firewall/edge migration are outside this checkpoint scope.

## Stop and restore after demo

Stop backends using CtrlC in their own tabs. Stop project nginx with nginx -p "$HOME/Documents/CN_Phase1/edge/" -c nginx.conf -s quit. For DNS, CtrlC may not stop it; use ps -axo pid,command to identify project dnsmasq and sudo kill -TERM CURRENT_PID, then verify exit. Restore Wi-Fi DNS using configs/DNS_Rollback.md when leaving hotspot. Do not run cleanup during a working demo.
