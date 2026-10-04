# Phase 1 — Client Certificate Trust Commands

## 1. Evidence Source

This document summarizes member-labelled terminal outputs supplied on **2026-10-03**.

All three members executed the certificate trust command using their verified public `server.crt` file. Each command returned to the shell prompt without a displayed error.

Exact command execution timestamps were not supplied.

## 2. Certificate Verification Before Trust

The public certificate copies on all three Macs had matching SHA-256 fingerprints.

The fingerprint comparison is documented in [Certificate Transfer Verification](21_certificate_transfer_verified.md).

## 3. Kartik — Trust Command

Kartik used the certificate stored under the nginx project directory:

```bash
sudo security add-trusted-cert \
  -d \
  -r trustRoot \
  -p ssl \
  -k /Library/Keychains/System.keychain \
  "$HOME/Documents/CN_Phase1/edge/certs/server.crt"
```

## 4. Nitin and Piyush — Trust Command

Each ran the following command on their own Mac:

```bash
sudo security add-trusted-cert \
  -d \
  -r trustRoot \
  -p ssl \
  -k /Library/Keychains/System.keychain \
  "$HOME/Documents/CN_Phase1/certs/server.crt"
```

## 5. Recorded Command Results

| Member | Certificate Location | Recorded Result |
|---|---|---|
| Kartik | ~/Documents/CN_Phase1/edge/certs/server.crt | Returned to prompt without a displayed error |
| Nitin | ~/Documents/CN_Phase1/certs/server.crt | Returned to prompt without a displayed error |
| Piyush | ~/Documents/CN_Phase1/certs/server.crt | Returned to prompt without a displayed error |

Administrator passwords were not supplied or stored in the evidence.

## 6. Subsequent HTTPS Verification

Command completion alone does not establish that HTTPS verification works.

Subsequent curl tests on all three Macs successfully validated the server certificate and returned HTTP 200 responses using installed trust, without `--cacert` or `-k`.

The recorded results are documented in [HTTPS System Trust Verification](23_https_system_trust_verified.md).

## 7. DNS Scope of the Tests

Kartik and Piyush used their configured project DNS settings for ordinary domain-based HTTPS requests.

Nitin left his system DNS settings unchanged and used curl's `--resolve` option to connect the project hostname to **10.63.169.72:8443**.

Nitin's test verifies HTTPS connectivity, hostname validation and certificate trust. It does not demonstrate a default DNS lookup for the project hostname.

## 8. Related Evidence

- [TLS Certificate Metadata](19_tls_certificate_metadata.md)
- [Certificate Transfer Verification](21_certificate_transfer_verified.md)
- [HTTPS System Trust Verification](23_https_system_trust_verified.md)
- [Default Client DNS Verification](13_default_dns_verified.md)
- [Client Trust Instructions](../configs/TLS_Client_Trust.md)
