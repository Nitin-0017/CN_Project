# HTTPS With System Certificate Trust

User supplied all three member-labelled curl outputs. No -k or --cacert used. All show TLSv1.3, AEAD-CHACHA20-POLY1305-SHA256, SAN matching app.teamcn.test, SSL certificate verify ok, ALPN http/1.1 and HTTP/1.1 200 OK via nginx/1.31.6. JSON status ok with matching backend identifier.

| Member | Resolution method | Backend | Response date UTC | Time IST |
|---|---|---|---|---|
| Nitin | --resolve app.teamcn.test:8443:10.63.169.72 | B | 2026-10-03 14:45:01 | 20:15:01 |
| Kartik | Normal hostname lookup | A | 2026-10-03 14:45:03 | 20:15:03 |
| Piyush | Normal hostname lookup | B | 2026-10-03 14:45:04 | 20:15:04 |

All responses: application/json, Content-Length 33, Cache-Control no-store. Nitin's test does not prove default DNS resolution; Kartik/Piyush normal DNS was independently verified. No browser warning-free test or original screenshots from this step received yet. Packet TLS handshake evidence remains Task G. The curl (304) handshake prefixes are TLS trace labels, not HTTP caching status codes.
