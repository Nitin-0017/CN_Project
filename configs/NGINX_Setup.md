# Phase 1 Nginx Setup

Kartik supplied successful nginx 1.31.6 installation, prefix /opt/homebrew and no output for the port 8080/8443 listener check. Original installation output retained in evidence/14_nginx_install_original.txt.

Standalone project prefix on Kartik: ~/Documents/CN_Phase1/edge/. Create logs/ and copy nginx-phase1-http.conf as nginx.conf. Does not use the Homebrew default nginx.conf or services.

```sh
nginx -t -p "$HOME/Documents/CN_Phase1/edge/" -c nginx.conf
nginx -p "$HOME/Documents/CN_Phase1/edge/" -c nginx.conf -g 'daemon off;'
```

Keep the nginx tab open. HTTP port 8080 is an intermediate routing test; final TLS demo will use 8443 and the domain with certificate validation. No TLS configuration yet. Default upstream method is round-robin. Passive failure detection/retry is configured; live failover remains untested. Two peers forward to A and B. X-Backend is passed through from backend responses.

From Piyush in a new terminal tab:

```sh
curl -i --connect-timeout 5 http://app.teamcn.test:8080/api/status
```

Run six times sequentially to show both A/B, ideally alternating with both healthy and no concurrent traffic. Capture all headers and JSON. Do not claim strict alternation with other concurrent requests.

Reference: https://nginx.org/en/docs/http/load_balancing.html
