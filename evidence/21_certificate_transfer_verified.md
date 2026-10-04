# Phase 1 — Public Certificate Transfer Verification

## 1. Evidence Source

This document summarizes member-labelled OpenSSL fingerprint outputs supplied on **2026-10-03**.

All three members reported the same SHA-256 fingerprint for their public `server.crt` file.

These results are transcribed terminal evidence.

## 2. Certificate Transfer and Locations

Kartik transferred the public certificate to Nitin and Piyush using AirDrop.

| Member | Public Certificate Location |
|---|---|
| Kartik Yadav | ~/Documents/CN_Phase1/edge/certs/server.crt |
| Nitin Kumar | ~/Documents/CN_Phase1/certs/server.crt |
| Piyush Yadav | ~/Documents/CN_Phase1/certs/server.crt |

The repository copy is available as [server.crt](../configs/server.crt).

## 3. Fingerprint Verification Commands

### Kartik

```bash
openssl x509 \
  -in "$HOME/Documents/CN_Phase1/edge/certs/server.crt" \
  -noout \
  -fingerprint \
  -sha256
```

### Nitin and Piyush

Each ran on their own Mac:

```bash
openssl x509 \
  -in "$HOME/Documents/CN_Phase1/certs/server.crt" \
  -noout \
  -fingerprint \
  -sha256
```

## 4. Recorded SHA-256 Fingerprint

All three reported:

```text
ED:D0:4D:21:98:8A:8C:84:B6:86:1B:76:31:9C:36:3B:71:7B:E5:B1:AD:7C:59:EE:5A:C6:E6:DC:1B:44:D4:C2
```

| Member | Fingerprint Comparison |
|---|---|
| Kartik | Reference fingerprint |
| Nitin | Matches Kartik |
| Piyush | Matches Kartik |

## 5. Interpretation

The matching SHA-256 fingerprints identify the same public certificate on all three Macs.

This verifies certificate consistency after transfer. Fingerprint equality alone does not prove that client trust was installed or that an HTTPS request succeeded.

## 6. Subsequent Trust and HTTPS Verification

Client trust installation was subsequently recorded, followed by successful HTTPS requests using installed trust without `--cacert` or `-k`.

Those results are documented separately:

- [Client Trust Commands](22_client_trust_commands.md)
- [HTTPS System Trust Verification](23_https_system_trust_verified.md)

## 7. Private Key Handling

Only the public `server.crt` was distributed.

The private `server.key` remains on Kartik's Mac for nginx and is excluded from the submission.

## 8. Related Documents

- [TLS Certificate Metadata](19_tls_certificate_metadata.md)
- [Explicit Certificate HTTPS Test](20_https_cacert_verified.md)
- [Client Trust Instructions](../configs/TLS_Client_Trust.md)
- [TLS Setup Instructions](../configs/TLS_Setup.md)
- [Verified TLS Packet Analysis](27_packet_analysis_verified.md)
