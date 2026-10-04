# Phase 1 — Backend HTTP Tests From Kartik

## 1. Evidence Source

These results summarize terminal outputs supplied on **2026-10-03**.

All four requests originated from Kartik's Mac and directly targeted the two backend servers on the project hotspot.

The timestamps below come from the HTTP response `Date` headers and are recorded in **UTC**.

This document contains transcribed results. Original screenshots of these four tests are not linked here.

## 2. Test Commands

Kartik ran each command separately:

```bash
curl -i --connect-timeout 5 http://10.63.169.3:3001/
```

```bash
curl -i --connect-timeout 5 http://10.63.169.3:3001/api/status
```

```bash
curl -i --connect-timeout 5 http://10.63.169.63:3002/
```

```bash
curl -i --connect-timeout 5 http://10.63.169.63:3002/api/status
```

## 3. Recorded Results

| Backend | URL | HTTP Status | X-Backend | Response Date (UTC) | Content-Length |
|---|---|---|---|---|---:|
| A | `http://10.63.169.3:3001/` | HTTP/1.1 200 OK | A | 2026-10-03 13:52:24 | 74 |
| A | `http://10.63.169.3:3001/api/status` | HTTP/1.1 200 OK | A | 2026-10-03 13:52:43 | 33 |
| B | `http://10.63.169.63:3002/` | HTTP/1.1 200 OK | B | 2026-10-03 13:53:00 | 74 |
| B | `http://10.63.169.63:3002/api/status` | HTTP/1.1 200 OK | B | 2026-10-03 13:53:10 | 33 |

## 4. Recorded Response Headers

All four responses included:

```http
Cache-Control: no-store
Content-Type: application/json; charset=utf-8
```

Backend A reported:

```http
Server: BaseHTTP/0.6 Python/3.13.1
X-Backend: A
```

Backend B reported:

```http
Server: BaseHTTP/0.6 Python/3.14.2
X-Backend: B
```

These are selected recorded headers, not complete response-header dumps.

## 5. Recorded JSON Content

### Backend A — Root Endpoint

```json
{"backend": "A", "message": "CN Phase 1 service running", "status": "ok"}
```

### Backend A — Status Endpoint

```json
{"backend": "A", "status": "ok"}
```

### Backend B — Root Endpoint

```json
{"backend": "B", "message": "CN Phase 1 service running", "status": "ok"}
```

### Backend B — Status Endpoint

```json
{"backend": "B", "status": "ok"}
```

## 6. Interpretation

All four requests returned **HTTP 200 OK**, with the correct backend identifier in both the `X-Backend` header and JSON body.

These tests verify that Kartik's Mac could reach Backend A on **10.63.169.3:3001** and Backend B on **10.63.169.63:3002**, and that both required endpoints responded correctly.

This establishes direct backend connectivity from the nginx host at the time of testing.

## 7. Test Scope

These requests used direct IP addresses over HTTP. DNS resolution, nginx load balancing and HTTPS certificate validation were tested separately.

The `/` and `/api/status` responses use `Cache-Control: no-store`. The conditional caching demonstration uses the separate `/api/cache` endpoint.

Final client demonstrations use the project domain through nginx HTTPS:

```text
https://app.teamcn.test:8443/api/status
```

## 8. Related Evidence

- [Backend Startup](07_backend_startup.md)
- [Backend Source Code](../backend/server.py)
- [HTTP Round-Robin Verification](17_http_round_robin_verified.md)
- [HTTPS System Trust Verification](23_https_system_trust_verified.md)
- [Conditional HTTP Caching](24_https_cache_304_verified.md)
- [Project Architecture](../docs/Architecture.md)
