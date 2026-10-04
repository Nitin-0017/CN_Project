# HTTPS Explicit Certificate Validation

Source: supplied Kartik terminal output and original screenshot, received 2026-10-03. Original saved as Kartik_HTTPS_cacert_test.jpg.

nginx HTTPS config validation passed and reload returned without reported error. curl -v --cacert local server.crt requested https://app.teamcn.test:8443/api/status. Host resolved to 10.63.169.72 and connected to TCP 8443.

Observed TLSv1.3, AEAD-CHACHA20-POLY1305-SHA256, ALPN accepted http/1.1. Certificate SAN matched app.teamcn.test and SSL certificate verify ok. HTTP/1.1 200 OK, nginx/1.31.6, X-Backend A, JSON {"backend":"A","status":"ok"}. Date 2026-10-03 14:34:49 UTC = 20:04:49 IST.

This is a certificate-validated test using explicit trust file, not a bypass. Client trust store configuration and ordinary curl/browser tests are still pending. The curl handshake line prefix (304) is not an HTTP 304 response; this request returned 200 and does not demonstrate HTTP caching.
