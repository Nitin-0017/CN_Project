# Phase 1 TLS Certificate Setup

Kartik: /opt/homebrew/bin/openssl, version 4.0.3 as supplied. Self-signed server certificate is permitted by the project brief. Generate locally on Kartik; private key must stay on Kartik and must not be shared or included in submission.

Create edge/certs/tls-server.cnf from the bundled template, then from edge/certs run:

```sh
umask 077
openssl req -x509 -newkey rsa:2048 -sha256 -noenc -days 90 -keyout server.key -out server.crt -config tls-server.cnf
openssl x509 -in server.crt -noout -subject -issuer -dates -ext subjectAltName
openssl x509 -in server.crt -noout -ext extendedKeyUsage
```

Expected SAN names app.teamcn.test and api.teamcn.test, serverAuth EKU. Certificate generation and supplied SAN/EKU/validity metadata verified. nginx HTTPS configuration prepared; runtime and client trust remain pending. Only public server.crt will later be distributed for explicit client trust. No local CA has been created.

## Add HTTPS to nginx

Back up edge/nginx.conf as nginx-http-backup.conf. Replace nginx.conf with bundled nginx-phase1-https.conf. Validate then reload in a separate tab while foreground nginx runs:

```sh
nginx -t -p "$HOME/Documents/CN_Phase1/edge/" -c nginx.conf
nginx -p "$HOME/Documents/CN_Phase1/edge/" -c nginx.conf -s reload
curl -v --cacert "$HOME/Documents/CN_Phase1/edge/certs/server.crt" --connect-timeout 5 --max-time 15 https://app.teamcn.test:8443/api/status
```

Explicit --cacert validates certificate and hostname; it does not bypass verification. This intermediate test does not replace the required trust-store configuration on each client. HTTP 8080 remains available for comparison; HTTPS demo uses 8443. Public cert transfer and client trust are later steps.
