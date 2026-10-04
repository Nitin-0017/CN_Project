# Self Signed TLS Certificate Metadata

Source: Kartik user-supplied OpenSSL generation and inspection output, received 2026-10-03. Generation returned to prompt without reported error.

Subject and issuer: CN=app.teamcn.test, O=CN Project Team. Matching issuer and subject are consistent with self-signed generation using openssl req -x509.

Validity: 2026-10-03 14:31:37 UTC (20:01:37 IST) through 2027-01-01 14:31:37 UTC (20:01:37 IST).

SAN: DNS:app.teamcn.test, DNS:api.teamcn.test.
EKU: TLS Web Server Authentication.
Generation parameters: RSA 2048, SHA-256, 90 days, unencrypted private key stored locally on Kartik under edge/certs/server.key with restrictive umask 077. Public certificate at edge/certs/server.crt. Neither key nor certificate content received by assistant; metadata only. Private key must not enter submission or messages.

HTTPS nginx runtime and client trust remain pending.
