# Phase 1 nginx Reverse Proxy and Load Balancing

Kartik's Mac runs nginx as the edge server. It accepts HTTP and HTTPS requests and forwards them to Backend A on Nitin's Mac and Backend B on Piyush's Mac.

## 1. Server Details

| Component | Machine | Address |
|---|---|---|
| nginx edge | Kartik | 10.63.169.72 |
| Backend A | Nitin | 10.63.169.3:3001 |
| Backend B | Piyush | 10.63.169.63:3002 |
| HTTP listener | Kartik | Port 8080 |
| HTTPS listener | Kartik | Port 8443 |

Project domains:

- `app.teamcn.test`
- `api.teamcn.test`

Both domains resolve to `10.63.169.72`.

The recorded nginx version was **1.31.6**. Recheck the machine IP addresses after reconnecting to the hotspot.

## 2. Install nginx — Kartik

If nginx is not already installed:

```bash
brew install nginx
```

The project uses a standalone configuration under:

```text
~/Documents/CN_Phase1/edge/
```

## 3. Project Directory Layout

```text
edge/
├── nginx.conf
├── certs/
│   ├── server.crt
│   └── server.key
└── logs/
    ├── access.log
    ├── error.log
    └── nginx.pid
```

Create the required directories:

```bash
mkdir -p ~/Documents/CN_Phase1/edge/logs
mkdir -p ~/Documents/CN_Phase1/edge/certs
```

Use the repository's `nginx-phase1-https.conf` as the runtime `edge/nginx.conf`.

The TLS certificate and matching private key must exist on Kartik's Mac before validating the HTTPS configuration. See [TLS Setup](TLS_Setup.md).

## 4. Final Tested Configuration

```nginx
worker_processes 1;
pid logs/nginx.pid;
error_log logs/error.log info;

events {
    worker_connections 256;
}

http {
    log_format project '$remote_addr "$request" $status upstream=$upstream_addr';
    access_log logs/access.log project;

    upstream cn_backends {
        server 10.63.169.3:3001 max_fails=1 fail_timeout=5s;
        server 10.63.169.63:3002 max_fails=1 fail_timeout=5s;
    }

    server {
        listen 8080;
        listen 8443 ssl;
        server_name app.teamcn.test api.teamcn.test;

        ssl_certificate certs/server.crt;
        ssl_certificate_key certs/server.key;
        ssl_protocols TLSv1.2 TLSv1.3;

        location / {
            proxy_pass http://cn_backends;
            proxy_http_version 1.1;
            proxy_set_header Host $host;
            proxy_set_header X-Real-IP $remote_addr;
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
            proxy_set_header X-Forwarded-Proto $scheme;
            proxy_connect_timeout 3s;
            proxy_read_timeout 10s;
            proxy_next_upstream error timeout http_502 http_503 http_504;
            proxy_next_upstream_tries 2;
        }
    }
}
```

## 5. Validate the Configuration — Kartik

```bash
nginx -t \
  -p "$HOME/Documents/CN_Phase1/edge/" \
  -c nginx.conf
```

Recorded output:

```text
nginx: the configuration file /Users/kartikyadav/Documents/CN_Phase1/edge/nginx.conf syntax is ok
nginx: configuration file /Users/kartikyadav/Documents/CN_Phase1/edge/nginx.conf test is successful
```

## 6. Start nginx — Kartik

```bash
nginx \
  -p "$HOME/Documents/CN_Phase1/edge/" \
  -c nginx.conf \
  -g 'daemon off;'
```

Keep this terminal open while running the demonstration.

For an already running project instance, validate changes first and then reload:

```bash
nginx -t \
  -p "$HOME/Documents/CN_Phase1/edge/" \
  -c nginx.conf

nginx \
  -p "$HOME/Documents/CN_Phase1/edge/" \
  -c nginx.conf \
  -s reload
```

## 7. HTTP Routing Test

Run from a client terminal:

```bash
curl -i --connect-timeout 5 --max-time 15 \
  http://app.teamcn.test:8080/api/status
```

HTTP on port 8080 was used to verify routing before HTTPS configuration.

An initial test had four timeouts followed by successful responses. A later six-request test returned HTTP 200 for every request with backend sequence A, B, A, B, A, B. The cause of the initial delay was not conclusively established.

## 8. HTTPS Verification

The client must use the private DNS server and trust the project certificate.

```bash
curl -v --connect-timeout 5 --max-time 15 \
  https://app.teamcn.test:8443/api/status
```

Recorded successful tests showed:

- Domain resolving to `10.63.169.72`
- Connection to nginx on port `8443`
- TLS 1.3 negotiation
- Certificate hostname matching `app.teamcn.test`
- `SSL certificate verify ok.`
- HTTP 200 response
- `X-Backend: A` or `X-Backend: B`

Certificate validation remained enabled.

## 9. Load Balancing Test

Run on Piyush's or Kartik's Mac:

```bash
for i in 1 2 3 4 5 6; do
  printf '\nRequest %s\n' "$i"
  curl -i --connect-timeout 5 --max-time 15 \
    https://app.teamcn.test:8443/api/status
done
```

nginx uses its default round-robin upstream method. The backend's `X-Backend` header is passed through to the client.

The recorded HTTPS recovery test returned six HTTP 200 responses with this sequence:

```text
B, B, A, B, A, B
```

Both backends appeared. This particular run did not show strict alternation for the first two requests.

## 10. Failure and Recovery Results

### Backend A Stopped

Nitin stopped Backend A. Piyush's six HTTPS requests all returned HTTP 200 with `X-Backend: B`.

After Backend A was restarted, subsequent requests returned responses from both A and B.

### Both Backends Stopped

With both backends stopped, nginx returned `502 Bad Gateway`.

DNS resolution and TLS certificate verification still succeeded. The failure occurred when nginx attempted to serve the request through its upstream backends.

After backend recovery, six requests returned HTTP 200 and both backend identifiers appeared.

## 11. Inspect Logs — Kartik

```bash
tail -n 30 ~/Documents/CN_Phase1/edge/logs/access.log
tail -n 30 ~/Documents/CN_Phase1/edge/logs/error.log
```

The access log records the client IP, request, response status and upstream address.

## 12. Stop nginx — Kartik

To stop the project instance gracefully from another terminal:

```bash
nginx \
  -p "$HOME/Documents/CN_Phase1/edge/" \
  -c nginx.conf \
  -s quit
```

## 13. Related Documentation

- [HTTPS nginx Configuration](nginx-phase1-https.conf)
- [Initial HTTP Configuration](nginx-phase1-http.conf)
- [TLS Setup](TLS_Setup.md)
- [Client Certificate Trust](TLS_Client_Trust.md)
- [Backend Setup](../backend/README.md)
- [Failure Demonstrations](../docs/07_Failure_Demonstrations.md)
- [Evidence Index](../evidence/INDEX.md)
