# Phase 1 Backend Services

Both backends use the same `server.py` with different backend identifiers and ports. The server uses Python 3.12 or later and the Python standard library; no additional packages are required.

## 1. Backend Machines

| Member | Backend | IP Address | Port |
|---|---|---|---|
| Nitin | A | 10.63.169.3 | 3001 |
| Piyush | B | 10.63.169.63 | 3002 |

These IP addresses were used during the recorded demonstration. Recheck them after reconnecting to the hotspot.

## 2. Start Backend A — Nitin

Run on Nitin's Mac:

```bash
cd ~/Documents/CN_Phase1/backend
python3 server.py --backend A --port 3001
```

Recorded startup output:

```text
Backend A listening on 0.0.0.0:3001
```

## 3. Start Backend B — Piyush

Run on Piyush's Mac:

```bash
cd ~/Documents/CN_Phase1/backend
python3 server.py --backend B --port 3002
```

Recorded startup output:

```text
Backend B listening on 0.0.0.0:3002
```

Keep each server terminal open while testing. Press `Ctrl+C` in that terminal to stop the backend. Allow incoming Python connections if macOS requests permission.

## 4. Available Endpoints

| Endpoint | Behaviour |
|---|---|
| `/` | Returns the service message, backend identifier and status |
| `/api/status` | Returns the backend identifier and status |
| `/api/cache` | Returns identical cacheable content from both backends |

Responses include the `X-Backend` header identifying backend A or B.

- `/` and `/api/status` use `Cache-Control: no-store`.
- `/api/cache` uses `Cache-Control: public, max-age=60` and an ETag.
- A matching `If-None-Match` request returns `304 Not Modified` without a response body.
- HEAD requests are supported.
- Unknown paths return `404 Not Found`.

## 5. Direct Backend Tests — Kartik

Run on Kartik's Mac to check LAN reachability:

```bash
curl -i --connect-timeout 5 http://10.63.169.3:3001/
curl -i --connect-timeout 5 http://10.63.169.3:3001/api/status

curl -i --connect-timeout 5 http://10.63.169.63:3002/
curl -i --connect-timeout 5 http://10.63.169.63:3002/api/status
```

All four recorded tests returned `HTTP/1.1 200 OK`, the correct `X-Backend` header and the expected JSON response.

## 6. Access Through nginx HTTPS

Kartik's nginx edge forwards requests to both backends. Client-facing HTTPS terminates at nginx; nginx connects to the backends using HTTP.

Use the private domain for the HTTPS demonstration:

```bash
curl -i --connect-timeout 5 --max-time 15 \
  https://app.teamcn.test:8443/api/status
```

The client must use the private DNS server and trust the project certificate. Certificate validation remains enabled.

## 7. Related Documentation

- [Architecture](../docs/Architecture.md)
- [Demo Guide](../docs/Demo_Guide.md)
- [Caching Test](../docs/05_Caching_Test.md)
- [Failure Demonstrations](../docs/07_Failure_Demonstrations.md)
- [Evidence Index](../evidence/INDEX.md)
