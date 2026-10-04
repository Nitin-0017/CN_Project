# Phase 1 TLS Certificate Setup

Kartik generated a self-signed server certificate for the project's nginx HTTPS edge. HTTPS configuration, certificate transfer, client trust and verification were completed on 3 October 2026.

## 1. Certificate and Server Details

| Item | Recorded Value |
|---|---|
| Edge server | Kartik — 10.63.169.72 |
| HTTPS port | 8443 |
| Certificate type | Self-signed server certificate |
| Key | RSA 2048-bit |
| Signature hash | SHA-256 |
| Validity | 90 days |
| Certificate file | server.crt |
| Private key file | server.key |

Certificate directory on Kartik's Mac:

```text
~/Documents/CN_Phase1/edge/certs/
```

The private key stays on Kartik's Mac. Only the public certificate is shared with clients.

## 2. Create the Certificate Configuration — Kartik

```bash
mkdir -p ~/Documents/CN_Phase1/edge/certs
cd ~/Documents/CN_Phase1/edge/certs
```

Create `tls-server.cnf`:

```bash
cat > tls-server.cnf <<'CONF'
[req]
prompt = no
distinguished_name = dn
x509_extensions = server_cert

[dn]
CN = app.teamcn.test
O = CN Project Team

[server_cert]
subjectAltName = DNS:app.teamcn.test,DNS:api.teamcn.test
basicConstraints = critical,CA:FALSE
keyUsage = critical,digitalSignature,keyEncipherment
extendedKeyUsage = serverAuth
CONF
```

The SAN entries allow the certificate to identify both project domains. `CA:FALSE` specifies a server certificate rather than a certificate authority.

## 3. Generate the Certificate — Kartik

The following commands were used during initial certificate creation:

```bash
umask 077

openssl req -x509 -newkey rsa:2048 -sha256 -noenc -days 90 \
  -keyout server.key \
  -out server.crt \
  -config tls-server.cnf
```

`umask 077` restricts permissions on newly created files. The private key is unencrypted so nginx can load it without an interactive passphrase.

Keep the existing certificate and matching key for the recorded setup. Regenerating them changes the certificate fingerprint and requires updating client trust.

## 4. Inspect the Certificate

```bash
openssl x509 -in server.crt \
  -noout -subject -issuer -dates -ext subjectAltName

openssl x509 -in server.crt \
  -noout -ext extendedKeyUsage
```

Recorded output:

```text
subject=CN=app.teamcn.test, O=CN Project Team
issuer=CN=app.teamcn.test, O=CN Project Team
notBefore=Oct  3 14:31:37 2026 GMT
notAfter=Jan  1 14:31:37 2027 GMT
X509v3 Subject Alternative Name:
    DNS:app.teamcn.test, DNS:api.teamcn.test
```

Extended key usage:

```text
X509v3 Extended Key Usage:
    TLS Web Server Authentication
```

The matching subject and issuer reflect the self-signed certificate. No separate local CA was created.

## 5. Configure nginx HTTPS

The final nginx server block includes:

```nginx
listen 8080;
listen 8443 ssl;
server_name app.teamcn.test api.teamcn.test;

ssl_certificate certs/server.crt;
ssl_certificate_key certs/server.key;
ssl_protocols TLSv1.2 TLSv1.3;
```

Certificate paths are relative to the project nginx prefix:

```text
~/Documents/CN_Phase1/edge/
```

The full reverse proxy and upstream configuration is available in:

[HTTPS nginx Configuration](nginx-phase1-https.conf)

## 6. Validate and Reload nginx — Kartik

With the HTTPS configuration saved as `edge/nginx.conf`:

```bash
nginx -t \
  -p "$HOME/Documents/CN_Phase1/edge/" \
  -c nginx.conf
```

Recorded validation result:

```text
nginx: the configuration file /Users/kartikyadav/Documents/CN_Phase1/edge/nginx.conf syntax is ok
nginx: configuration file /Users/kartikyadav/Documents/CN_Phase1/edge/nginx.conf test is successful
```

Reload the already running project instance:

```bash
nginx \
  -p "$HOME/Documents/CN_Phase1/edge/" \
  -c nginx.conf \
  -s reload
```

If the project instance is stopped, start it instead:

```bash
nginx \
  -p "$HOME/Documents/CN_Phase1/edge/" \
  -c nginx.conf \
  -g 'daemon off;'
```

## 7. Initial Certificate Verification — Kartik

Kartik first tested HTTPS using the public certificate explicitly:

```bash
curl -v \
  --cacert "$HOME/Documents/CN_Phase1/edge/certs/server.crt" \
  --connect-timeout 5 --max-time 15 \
  https://app.teamcn.test:8443/api/status
```

The recorded test confirmed:

- TLS 1.3 negotiation
- Certificate SAN matching `app.teamcn.test`
- `SSL certificate verify ok.`
- HTTP 200
- `X-Backend: A`

The `--cacert` option supplies a trusted certificate for this request while retaining certificate and hostname verification.

## 8. Certificate Transfer and Client Trust

Kartik transferred only `server.crt` to Nitin and Piyush using AirDrop.

All three Macs reported this SHA-256 fingerprint:

```text
ED:D0:4D:21:98:8A:8C:84:B6:86:1B:76:31:9C:36:3B:71:7B:E5:B1:AD:7C:59:EE:5A:C6:E6:DC:1B:44:D4:C2
```

The certificate was then explicitly trusted for SSL in each Mac's System keychain.

Commands and verification results are documented in:

[Client Certificate Trust](TLS_Client_Trust.md)

## 9. Final HTTPS Verification

After installing certificate trust, Kartik and Piyush ran:

```bash
curl -v --connect-timeout 5 --max-time 15 \
  https://app.teamcn.test:8443/api/status
```

Nitin used `--resolve` because his system DNS settings were not changed:

```bash
curl -v \
  --resolve app.teamcn.test:8443:10.63.169.72 \
  --connect-timeout 5 --max-time 15 \
  https://app.teamcn.test:8443/api/status
```

All three tests passed certificate verification and returned HTTP 200. These final tests used neither `--cacert` nor `--insecure`.

Nitin's `--resolve` test verified HTTPS connectivity and certificate trust; it did not test default DNS resolution.

## 10. TLS Packet Capture

Piyush selected TLS 1.2 for the Wireshark demonstration:

```bash
curl -v --tlsv1.2 --tls-max 1.2 \
  --connect-timeout 5 --max-time 15 \
  https://app.teamcn.test:8443/api/status
```

The capture shows Client Hello, Server Hello, Certificate, key exchange, Change Cipher Spec and encrypted Application Data.

The certificate extracted from frame 27 matched the project's verified fingerprint.

![TLS handshake and encrypted application data](../evidence/Piyush_Wireshark_TLS.jpg)

See [Packet Capture Documentation](../docs/06_Packet_Capture.md) for the complete analysis.

## 11. Supporting Evidence

- [Certificate Metadata](../evidence/19_tls_certificate_metadata.md)
- [Initial HTTPS Certificate Verification](../evidence/20_https_cacert_verified.md)
- [Certificate Transfer Verification](../evidence/21_certificate_transfer_verified.md)
- [Client Trust Commands](../evidence/22_client_trust_commands.md)
- [Final HTTPS Trust Verification](../evidence/23_https_system_trust_verified.md)
- [nginx Setup](NGINX_Setup.md)
