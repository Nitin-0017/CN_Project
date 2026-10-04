# HTTP Round Robin Repeat Verification

User-supplied Piyush curl -v output. Target http://app.teamcn.test:8080/api/status resolved to 10.63.169.72. All six connected to port 8080 and returned HTTP/1.1 200 OK from nginx/1.31.6 with matching backend JSON. Response dates 2026-10-03 14:26:17 UTC = 19:56:17 IST.

| Request | X-Backend | DNS s | Connect s | First byte s | Total s | Status |
|---|---|---|---|---|---|---|
| 1 | A | 0.017486 | 0.127324 | 0.195703 | 0.195800 | 200 |
| 2 | B | 0.002920 | 0.009884 | 0.062047 | 0.062088 | 200 |
| 3 | A | 0.002210 | 0.009407 | 0.031339 | 0.031388 | 200 |
| 4 | B | 0.002425 | 0.008563 | 0.027880 | 0.027906 | 200 |
| 5 | A | 0.001703 | 0.008109 | 0.028836 | 0.028870 | 200 |
| 6 | B | 0.002381 | 0.008368 | 0.028974 | 0.029006 | 200 |

All responses Content-Type application/json; charset=utf-8, Content-Length 33 and Cache-Control no-store. Round-robin distribution A/B/A/B/A/B demonstrated. Timings are cumulative curl milestones, not separate independent stage durations. No configuration change was reported between initial mixed results and this successful repeat. Earlier timeout cause remains unknown; nginx logs are pending. This successful sample does not establish long-term reliability. HTTPS still pending.
