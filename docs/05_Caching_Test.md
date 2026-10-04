# Phase 1 HTTP Caching and ETag Validation

Piyush tested HTTP caching headers and conditional validation through nginx HTTPS on 3 October 2026.

The first request returned HTTP 200 from Backend B. A subsequent request with the matching ETag returned HTTP 304 from Backend A without a response body.

## 1. Test Setup

| Item | Value |
|---|---|
| Test client | Piyush — 10.63.169.63 |
| HTTPS edge | Kartik — 10.63.169.72:8443 |
| Endpoint | https://app.teamcn.test:8443/api/cache |
| Cache-Control | public, max-age=60 |

Both backends return identical content and ETags for `/api/cache`, allowing conditional validation to work across the load-balanced servers.

The `/api/status` endpoint uses `Cache-Control: no-store`.

## 2. First Request — Save Headers and Body

Run on Piyush's Mac with DNS, nginx and both backends running:

```bash
mkdir -p ~/Documents/CN_Phase1/evidence

curl -sS \
  -D "$HOME/Documents/CN_Phase1/evidence/cache-first.headers" \
  -o "$HOME/Documents/CN_Phase1/evidence/cache-first.json" \
  --connect-timeout 5 --max-time 15 \
  https://app.teamcn.test:8443/api/cache
```

Display the saved response:

```bash
cat ~/Documents/CN_Phase1/evidence/cache-first.headers
cat ~/Documents/CN_Phase1/evidence/cache-first.json
```

### Recorded Response Headers

```text
HTTP/1.1 200 OK
Server: nginx/1.31.6
Date: Sat, 03 Oct 2026 14:47:14 GMT
Content-Type: application/json; charset=utf-8
Content-Length: 73
Connection: keep-alive
X-Backend: B
Cache-Control: public, max-age=60
ETag: "b80d47eec1d7c70fd74370ea406e78b8c98e4b022801f19211e18c548d169f61"
```

### Recorded Response Body

```json
{"project": "CN Phase 1", "resource": "shared-cache-demo", "version": 1}
```

## 3. Extract the ETag

```bash
CN_ETAG=$(awk 'tolower($1)=="etag:" {sub(/\r$/, "", $2); print $2; exit}' \
  "$HOME/Documents/CN_Phase1/evidence/cache-first.headers")

printf 'ETag: %s\n' "$CN_ETAG"
```

Recorded value:

```text
ETag: "b80d47eec1d7c70fd74370ea406e78b8c98e4b022801f19211e18c548d169f61"
```

Confirm that the extracted ETag is not empty before sending the conditional request.

## 4. Send the Conditional Request

```bash
curl -i --connect-timeout 5 --max-time 15 \
  -H "If-None-Match: $CN_ETAG" \
  https://app.teamcn.test:8443/api/cache
```

### Recorded Response

```text
HTTP/1.1 304 Not Modified
Server: nginx/1.31.6
Date: Sat, 03 Oct 2026 14:47:52 GMT
Connection: keep-alive
X-Backend: A
Cache-Control: public, max-age=60
ETag: "b80d47eec1d7c70fd74370ea406e78b8c98e4b022801f19211e18c548d169f61"
```

No response body was returned.

## 5. What the Headers Mean

### Cache-Control

`public` allows browsers and shared caches to store the response.

`max-age=60` allows a stored response to be treated as fresh for 60 seconds. A cache can reuse a fresh response without contacting the server.

Once stale, the response can be revalidated using its ETag.

### ETag and If-None-Match

The ETag identifies the returned representation. The client sends its saved value in `If-None-Match`.

If the representation still matches, the server returns `304 Not Modified`, allowing the client to reuse its stored body. If it has changed, the server returns the new representation with HTTP 200.

## 6. What This Test Proves

- The first response contained cache directives and an ETag.
- Both backends used the same ETag for the shared resource.
- A matching conditional request returned HTTP 304 without a body.
- Conditional validation worked through nginx HTTPS across different backends.

The conditional request was sent approximately 38 seconds after the first response. It explicitly tested ETag validation; it did not wait for the 60-second freshness lifetime to expire.

Curl does not automatically maintain a browser-style response cache. This test demonstrates conditional validation, rather than an automatic browser cache hit or nginx proxy-cache hit.

## 7. Screenshot Evidence

The screenshot includes the initial HTTP 200 response, saved body, extracted ETag, conditional request and HTTP 304 response.

![Piyush HTTPS caching and conditional 304 response](../evidence/Piyush_HTTPS_cache_304.jpg)

## 8. Related Evidence

- [Recorded Cache Test](../evidence/24_https_cache_304_verified.md)
- [Backend Implementation](../backend/server.py)
- [nginx Setup](../configs/NGINX_Setup.md)
- [Client Certificate Trust](../configs/TLS_Client_Trust.md)
