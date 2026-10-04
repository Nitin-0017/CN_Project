# Backend HTTP Tests From Kartik

User-supplied terminal output received 2026-10-03. All requests originated on Kartik's Mac and used curl -i --connect-timeout 5.

| URL | Status | X-Backend | Response Date UTC | Content-Length |
|---|---|---|---|---|
| http://10.63.169.3:3001/ | HTTP/1.1 200 OK | A | 2026-10-03 13:52:24 | 74 |
| http://10.63.169.3:3001/api/status | HTTP/1.1 200 OK | A | 2026-10-03 13:52:43 | 33 |
| http://10.63.169.63:3002/ | HTTP/1.1 200 OK | B | 2026-10-03 13:53:00 | 74 |
| http://10.63.169.63:3002/api/status | HTTP/1.1 200 OK | B | 2026-10-03 13:53:10 | 33 |

All responses: Cache-Control: no-store; Content-Type: application/json; charset=utf-8. A reports BaseHTTP/0.6 Python/3.13.1; B reports BaseHTTP/0.6 Python/3.14.2.

Root JSON: {"backend": "A/B", "message": "CN Phase 1 service running", "status": "ok"}. Status JSON: {"backend": "A/B", "status": "ok"}, with the matching actual A or B identifier.

This confirms LAN access from the future nginx edge to both backend endpoints. These are setup tests; final client access must use the domain through HTTPS nginx. Caching behavior is not tested by these no-store endpoints. Original screenshots not received.
