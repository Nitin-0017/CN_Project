# Trust Project Certificate on macOS Clients

Kartik transfers only public server.crt from ~/Documents/CN_Phase1/edge/certs/ to Nitin and Piyush using AirDrop. Store received certificate as ~/Documents/CN_Phase1/certs/server.crt. Never transfer server.key.

Record SHA-256 fingerprint on Kartik and compare on recipients before trusting:

```sh
openssl x509 -in PATH_TO_SERVER_CRT -noout -fingerprint -sha256
```

For the self-signed project server certificate, add explicit SSL trust in System keychain:

Kartik:
```sh
sudo security add-trusted-cert -d -r trustRoot -p ssl -k /Library/Keychains/System.keychain "$HOME/Documents/CN_Phase1/edge/certs/server.crt"
```

Nitin and Piyush:
```sh
sudo security add-trusted-cert -d -r trustRoot -p ssl -k /Library/Keychains/System.keychain "$HOME/Documents/CN_Phase1/certs/server.crt"
```

Kartik/Piyush ordinary test:
```sh
curl -v --connect-timeout 5 --max-time 15 https://app.teamcn.test:8443/api/status
```

Nitin has not changed DNS settings; test without altering them:
```sh
curl -v --resolve app.teamcn.test:8443:10.63.169.72 --connect-timeout 5 --max-time 15 https://app.teamcn.test:8443/api/status
```

Nitin's --resolve test validates hostname/trust and service connectivity but is not evidence of default DNS lookup. Tests above use no -k or --cacert. Public certificate transfer verified by identical SHA-256 fingerprints on all three Macs. Trust installation and ordinary HTTPS results pending. GUI alternative is Keychain Access > certificate > Trust > SSL Always Trust.

Cleanup after project: record the public certificate SHA-1 fingerprint and remove that exact project certificate from System keychain; do not remove other certificates. Instructions will be finalised with the actual certificate fingerprint.

Verified public certificate SHA-256: ED:D0:4D:21:98:8A:8C:84:B6:86:1B:76:31:9C:36:3B:71:7B:E5:B1:AD:7C:59:EE:5A:C6:E6:DC:1B:44:D4:C2
