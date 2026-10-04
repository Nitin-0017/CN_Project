# Trust the Project TLS Certificate on macOS

The project uses a self-signed server certificate for `app.teamcn.test` and `api.teamcn.test`.

The certificate was explicitly trusted on all three Macs. Subsequent HTTPS tests passed certificate verification and returned HTTP 200.

## 1. Transfer the Public Certificate

Kartik transferred `server.crt` to Nitin and Piyush using AirDrop.

### Certificate Locations

| Machine | Location |
|---|---|
| Kartik | ~/Documents/CN_Phase1/edge/certs/server.crt |
| Nitin | ~/Documents/CN_Phase1/certs/server.crt |
| Piyush | ~/Documents/CN_Phase1/certs/server.crt |

Only the public certificate was shared. The private key `server.key` remains on Kartik's edge server.

## 2. Verify the Certificate Fingerprint

### Kartik

```bash
openssl x509 \
  -in "$HOME/Documents/CN_Phase1/edge/certs/server.crt" \
  -noout -fingerprint -sha256
```

### Nitin and Piyush

Run on each Mac:

```bash
openssl x509 \
  -in "$HOME/Documents/CN_Phase1/certs/server.crt" \
  -noout -fingerprint -sha256
```

### Recorded Result

All three Macs reported the same SHA-256 fingerprint:

```text
ED:D0:4D:21:98:8A:8C:84:B6:86:1B:76:31:9C:36:3B:71:7B:E5:B1:AD:7C:59:EE:5A:C6:E6:DC:1B:44:D4:C2
```

The matching fingerprints confirmed that the received certificate was identical to Kartik's certificate.

## 3. Install Certificate Trust — Kartik

Run on Kartik's Mac:

```bash
sudo security add-trusted-cert \
  -d -r trustRoot -p ssl \
  -k /Library/Keychains/System.keychain \
  "$HOME/Documents/CN_Phase1/edge/certs/server.crt"
```

## 4. Install Certificate Trust — Nitin and Piyush

Run on each Mac:

```bash
sudo security add-trusted-cert \
  -d -r trustRoot -p ssl \
  -k /Library/Keychains/System.keychain \
  "$HOME/Documents/CN_Phase1/certs/server.crt"
```

These commands add explicit SSL trust for the project certificate in the System keychain.

The recorded commands completed without reported errors. Successful HTTPS tests subsequently verified that the certificate was accepted.

## 5. HTTPS Test — Kartik and Piyush

Both clients had their Wi-Fi DNS configured to use Nitin's private DNS server `10.63.169.3`.

Run on each client:

```bash
curl -v --connect-timeout 5 --max-time 15 \
  https://app.teamcn.test:8443/api/status
```

Recorded results confirmed:

- Domain resolved to `10.63.169.72`.
- Connection reached nginx on port `8443`.
- TLS 1.3 was negotiated.
- The certificate SAN matched `app.teamcn.test`.
- Curl reported `SSL certificate verify ok.`
- The server returned `HTTP/1.1 200 OK`.
- The response included `X-Backend: A` or `X-Backend: B`.

## 6. HTTPS Test — Nitin

Nitin's system DNS settings were not changed for the project.

The following command supplied the edge IP for this request while retaining the domain name and TLS certificate validation:

```bash
curl -v \
  --resolve app.teamcn.test:8443:10.63.169.72 \
  --connect-timeout 5 --max-time 15 \
  https://app.teamcn.test:8443/api/status
```

The recorded request negotiated TLS 1.3, passed certificate verification and returned HTTP 200 with `X-Backend: B`.

The `--resolve` option overrides name resolution for this request. It does not disable TLS validation and is not evidence of a default DNS lookup.

## 7. Certificate Details

| Property | Recorded Value |
|---|---|
| Subject | CN=app.teamcn.test, O=CN Project Team |
| Issuer | CN=app.teamcn.test, O=CN Project Team |
| SAN | app.teamcn.test, api.teamcn.test |
| Valid From | 3 October 2026, 14:31:37 GMT |
| Valid Until | 1 January 2027, 14:31:37 GMT |
| Extended Key Usage | TLS Web Server Authentication |

The certificate is self-signed, so the subject and issuer are identical.

## 8. Verified Outcome

All three Macs successfully accessed the project HTTPS service with certificate verification enabled.

The final trust tests used neither `--insecure` nor `--cacert`. Kartik and Piyush used their configured private DNS; Nitin used `--resolve`.

## 9. Supporting Evidence

- [Certificate Transfer and Fingerprint Verification](../evidence/21_certificate_transfer_verified.md)
- [Client Trust Commands](../evidence/22_client_trust_commands.md)
- [HTTPS System Trust Verification](../evidence/23_https_system_trust_verified.md)
- [TLS Certificate Creation](TLS_Setup.md)
- [nginx Configuration](NGINX_Setup.md)
