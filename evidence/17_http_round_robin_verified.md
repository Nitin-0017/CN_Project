# Phase 1 — HTTP Round-Robin Repeat Verification

## 1. Evidence Source

This document summarizes Piyush's supplied verbose curl output from the successful repeat test on **2026-10-03**.

All six requests targeted:

```text
http://app.teamcn.test:8080/api/status
```

The hostname resolved to **10.63.169.72**, and all six requests connected to nginx on port **8080**.

Recorded response Date headers were **2026-10-03 14:26:17 UTC**, equivalent to **19:56:17 IST**.

This document contains transcribed terminal results.

## 2. Recorded Results

All timing values are in **seconds**.

| Request | X-Backend | DNS Lookup | TCP Connection | First Byte | Total Time | HTTP Status |
|---|---|---:|---:|---:|---:|---:|
| 1 | A | 0.017486 | 0.127324 | 0.195703 | 0.195800 | 200 |
| 2 | B | 0.002920 | 0.009884 | 0.062047 | 0.062088 | 200 |
| 3 | A | 0.002210 | 0.009407 | 0.031339 | 0.031388 | 200 |
| 4 | B | 0.002425 | 0.008563 | 0.027880 | 0.027906 | 200 |
| 5 | A | 0.001703 | 0.008109 | 0.028836 | 0.028870 | 200 |
| 6 | B | 0.002381 | 0.008368 | 0.028974 | 0.029006 | 200 |

## 3. Recorded Response Details

All six responses returned:

```http
HTTP/1.1 200 OK
Server: nginx/1.31.6
Content-Type: application/json; charset=utf-8
Content-Length: 33
Cache-Control: no-store
```

Each response included the matching `X-Backend` identifier and JSON body.

### Backend A

```http
X-Backend: A
```

```json
{"backend": "A", "status": "ok"}
```

### Backend B

```http
X-Backend: B
```

```json
{"backend": "B", "status": "ok"}
```

The header block above lists selected common response fields, not a complete header dump.

## 4. Round-Robin Observation

The recorded backend sequence was:

```text
A → B → A → B → A → B
```

All six requests returned **HTTP 200 OK**.

This sample demonstrates successful request forwarding through nginx and distribution across both backends, consistent with the configured round-robin upstream.

The exact sequence in another test may differ when concurrent requests or backend failures affect upstream selection.

## 5. Timing Interpretation

The recorded curl timing fields are cumulative milestones measured from the start of each request:

- **DNS Lookup:** time until name resolution completed.
- **TCP Connection:** time until the connection to nginx was established.
- **First Byte:** time until the first response byte arrived.
- **Total Time:** time until the request completed.

These values are not separate stage durations and should not be added together.

## 6. Relationship to the Initial Test

The earlier test recorded four timeouts followed by successful responses from A and B.

No configuration change was reported between that initial test and this successful repeat. The cause of the earlier timeouts remains unknown.

This repeat confirms six successful requests in the recorded sample; it does not establish long-term reliability.

## 7. Subsequent Verification

nginx log findings were subsequently recorded separately.

HTTPS was also configured and verified on port **8443**, with certificate validation and successful responses documented in the linked evidence below.

## 8. Related Evidence

- [nginx Validation and Launch](15_nginx_validation_launch.md)
- [Initial HTTP Load-Balancing Test](16_initial_http_load_balancing.md)
- [nginx Log Findings](18_log_findings.md)
- [Original nginx Logs](18_nginx_logs_openssl_original.txt)
- [HTTPS System Trust Verification](23_https_system_trust_verified.md)
- [Single Backend Failure and Recovery](30_single_backend_failover.md)
- [Final Project Status](../docs/Progress.md)
