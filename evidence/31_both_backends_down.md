# Both Backends Down Demonstration

Kartik supplied terminal output and original screenshot, saved as Kartik_both_backends_down.jpg, following instructions to stop both backends.

DNS at2026-10-03 20:59:21 IST returned NOERROR, A10.63.169.72, TTL60, SERVER10.63.169.3#53, query19ms, ID17244.

HTTPS request to app.teamcn.test:8443 connected and negotiated TLS1.3. SAN matched and SSL certificate verify ok without -k/--cacert. nginx1.31.6 returned HTTP/1.1 502 Bad Gateway, HTML error body157 bytes, Date2026-10-03 15:29:31 UTC=20:59:31 IST.

DNS, TCP and TLS edge connectivity remain functional while application upstream availability fails. This proves the layer separation expected by the brief. Separate backend stop screenshots not supplied for this scenario. Recovery verified: Kartik six subsequent HTTPS requests all HTTP200, backend sequence B/B/A/B/A/B at2026-10-03 15:32:35-36 UTC=21:02:35-36 IST. Recovery originals saved as Kartik_both_backends_recovery_1.jpg and _2.jpg. Both-down failure and restoration complete.
