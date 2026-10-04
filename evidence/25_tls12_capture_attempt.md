# TLS 1.2 Capture Attempt

Piyush dig app.teamcn.test A at 2026-10-03 20:25:37 IST returned NOERROR, A 10.63.169.72, TTL 60, server 10.63.169.3#53, query time 13 ms, ID 17924.

curl --tlsv1.2 --tls-max 1.2 to https://app.teamcn.test:8443/api/status passed hostname/certificate verification, negotiated TLSv1.2 ECDHE-RSA-CHACHA20-POLY1305 with HTTP/1.1, and returned 200 OK backend A at 2026-10-03 14:55:48 UTC = 20:25:48 IST. No bypass flag.

Supplied Wireshark screenshot still displays initial background IPv6/443 and mDNS packet list. Fresh project capture and save are not confirmed. Terminal TLS trace is not a substitute for captured packet evidence. Task G remains pending; request Capture menu/options screenshot to resolve current UI state.
