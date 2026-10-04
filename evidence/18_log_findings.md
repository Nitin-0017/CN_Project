# Nginx Log Findings

Original supplied logs preserved in 18_nginx_logs_openssl_original.txt. Access log contains four 499 GET entries alternating upstream A/B, then successful 200 A/B entries. Error log reports client prematurely closed connection while connecting to upstream. This is consistent with curl abandoning the initial requests at its time limit; root cause of delay is not proven.

Separate 400 requests begin with escaped bytes 16 03 01, consistent with TLS ClientHello traffic sent to the plain HTTP listener. This is a protocol mismatch inference; the source application is not identified. These entries are distinct from the four GET/499 requests and do not establish their cause. Use http:// with port 8080 until HTTPS listener is configured.

OpenSSL output: command -v = /opt/homebrew/bin/openssl; version OpenSSL 4.0.3 29 Sep 2026, library same. Successful repeat GET responses already verified. TLS setup next.
