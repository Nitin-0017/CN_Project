# Initial HTTP Load Balancing Test

Source: user-supplied Piyush terminal output and original image, received 2026-10-03. Image saved unchanged as Piyush_HTTP_load_balancing_initial.jpg.

Six sequential requests to http://app.teamcn.test:8080/api/status using curl -i --connect-timeout 5 --max-time 15.

| Request | Result |
|---|---|
| 1 | curl 28, timeout 15006 ms, 0 bytes |
| 2 | curl 28, timeout 15006 ms, 0 bytes |
| 3 | curl 28, timeout 15004 ms, 0 bytes |
| 4 | curl 28, timeout 15006 ms, 0 bytes |
| 5 | HTTP/1.1 200 OK, nginx/1.31.6, X-Backend A |
| 6 | HTTP/1.1 200 OK, nginx/1.31.6, X-Backend B |

Both successful responses dated 2026-10-03 14:23:28 UTC (19:53:28 IST), application/json, Content-Length 33, Cache-Control no-store, and matching backend/status JSON.

Domain routing to both backends demonstrated for two requests. Reliability unresolved because four of six requests timed out. Timeout cause not established; no DNS/firewall/upstream conclusion can be drawn from these outputs alone. Repeat with curl timing/verbose error details and nginx logs. Task D remains partial; HTTPS not configured.
