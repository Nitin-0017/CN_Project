# Phase 1 — Self-Signed TLS Certificate Metadata

## 1. Evidence Source

This document summarizes Kartik's OpenSSL certificate generation and inspection outputs supplied on **2026-10-03**.

Certificate generation returned to the shell prompt without a reported error. The public certificate was subsequently supplied and its SHA-256 fingerprint verified.

## 2. Certificate Identity

| Field | Recorded Value |
|---|---|
| Certificate type | Self-signed server certificate |
| Subject Common Name | app.teamcn.test |
| Subject Organization | CN Project Team |
| Issuer Common Name | app.teamcn.test |
| Issuer Organization | CN Project Team |

The matching subject and issuer are consistent with the recorded self-signed generation using `openssl req -x509`.

## 3. Certificate Validity

| Field | UTC | IST |
|---|---|---|
| Valid from | 2026-10-03 14:31:37 | 2026-10-03 20:01:37 |
| Valid until | 2027-01-01 14:31:37 | 2027-01-01 20:01:37 |

The certificate was generated with a validity period of **90 days**.

## 4. Subject Alternative Names

The certificate contains these DNS names:

```text
DNS:app.teamcn.test
DNS:api.teamcn.test
```

Both project hostnames are included for hostname validation.

## 5. Extended Key Usage

Recorded Extended Key Usage:

```text
TLS Web Server Authentication
```

This corresponds to `serverAuth`.

## 6. Generation Parameters and File Locations

| Item | Recorded Value |
|---|---|
| Key algorithm | RSA |
| Key size | 2048 bits |
| Signature digest | SHA-256 |
| Requested validity | 90 days |
| File creation umask | 077 |
| Private key encryption | Unencrypted |

Files generated on Kartik's Mac:

```text
~/Documents/CN_Phase1/edge/certs/server.crt
~/Documents/CN_Phase1/edge/certs/server.key
```

The public certificate is included as [server.crt](../configs/server.crt).

The private key remains on Kartik's Mac and is excluded from the submission.

## 7. SHA-256 Fingerprint

The verified public certificate fingerprint is:

```text
ED:D0:4D:21:98:8A:8C:84:B6:86:1B:76:31:9C:36:3B:71:7B:E5:B1:AD:7C:59:EE:5A:C6:E6:DC:1B:44:D4:C2
```

The certificate copies on all three Macs had matching fingerprints. Certificate transfer results are recorded separately.

## 8. Inspection Commands

Run from Kartik's certificate directory:

```bash
openssl x509 -in server.crt -noout -subject -issuer -dates
```

```bash
openssl x509 -in server.crt -noout -ext subjectAltName
```

```bash
openssl x509 -in server.crt -noout -ext extendedKeyUsage
```

```bash
openssl x509 -in server.crt -noout -fingerprint -sha256
```

## 9. Subsequent HTTPS Verification

The certificate was configured in nginx for HTTPS on port **8443**.

Subsequent evidence records:

- Successful HTTPS verification using the explicit public certificate.
- Transfer of the public certificate with matching fingerprints.
- Client trust configuration on all three Macs.
- Successful HTTPS requests using installed trust, without `curl -k`.
- A server certificate in the TLS packet capture matching the public certificate fingerprint.

Certificate metadata alone does not prove successful HTTPS operation; those runtime results are documented separately.

## 10. Related Evidence

- [TLS Generation Configuration](../configs/tls-server.cnf)
- [TLS Setup Instructions](../configs/TLS_Setup.md)
- [HTTPS Certificate Verification](20_https_cacert_verified.md)
- [Certificate Transfer Verification](21_certificate_transfer_verified.md)
- [Client Trust Commands](22_client_trust_commands.md)
- [HTTPS System Trust Verification](23_https_system_trust_verified.md)
- [Verified TLS Packet Analysis](27_packet_analysis_verified.md)
