# Public Certificate Transfer Verification

User-supplied openssl x509 -noout -fingerprint -sha256 outputs received 2026-10-03. All three members reported identical fingerprint:

ED:D0:4D:21:98:8A:8C:84:B6:86:1B:76:31:9C:36:3B:71:7B:E5:B1:AD:7C:59:EE:5A:C6:E6:DC:1B:44:D4:C2

Kartik certificate path: ~/Documents/CN_Phase1/edge/certs/server.crt.
Nitin and Piyush certificate path: ~/Documents/CN_Phase1/certs/server.crt.

SHA-256 equality confirms the supplied fingerprints identify the same public certificate. Trust installation and ordinary HTTPS verification are pending. Private key was not requested or received.
