# Phase 1 — HTTPS With System Certificate Trust

## 1. Evidence Source

This document summarizes member-labelled curl outputs from all three Macs, supplied on **2026-10-03**.

The requests used installed certificate trust. Neither `-k` nor `--cacert` was used.

This document records terminal transcriptions. Original screenshots of these specific three requests are not linked here.

## 2. HTTPS Test Commands

### Kartik and Piyush

Each ran on their own Mac:

```bash
curl -v \
  --connect-timeout 5 \
  --max-time 15 \
  https://app.teamcn.test:8443/api/status
```

### Nitin

Nitin kept his system DNS settings unchanged and ran:

```bash
curl -v \
  --resolve app.teamcn.test:8443:10.63.169.72 \
  --connect-timeout 5 \
  --max-time 15 \
  https://app.teamcn.test:8443/api/status
```

The `--resolve` option directs this hostname and port to the specified IP while retaining the hostname for TLS verification.

## 3. Common Recorded TLS Results

All three outputs recorded:

| Field | Result |
|---|---|
| Destination | 10.63.169.72:8443 |
| Negotiated TLS version | TLSv1.3 |
| Reported cipher | AEAD-CHACHA20-POLY1305-SHA256 |
| Certificate hostname match | app.teamcn.test matched the SAN |
| Certificate verification | SSL certificate verify ok |
| ALPN-selected protocol | http/1.1 |
| HTTP status | HTTP/1.1 200 OK |
| Server | nginx/1.31.6 |

## 4. Recorded Response Results

Dates and times below come from the HTTP response `Date` headers.

| Member | Address Selection Method | X-Backend | Response Date (UTC) | Equivalent Time (IST) |
|---|---|---|---|---|
| Nitin | Explicit curl `--resolve` mapping | B | 2026-10-03 14:45:01 | 2026-10-03 20:15:01 |
| Kartik | Normal hostname lookup | A | 2026-10-03 14:45:03 | 2026-10-03 20:15:03 |
| Piyush | Normal hostname lookup | B | 2026-10-03 14:45:04 | 2026-10-03 20:15:04 |

All responses included:

```http
Content-Type: application/json; charset=utf-8
Content-Length: 33
Cache-Control: no-store
```

The JSON bodies reported `"status": "ok"` and the matching backend identifier.

### Backend A Response

```json
{"backend": "A", "status": "ok"}
```

### Backend B Response

```json
{"backend": "B", "status": "ok"}
```

## 5. Interpretation

All three Macs successfully verified the certificate and hostname using installed trust and received HTTP 200 responses through nginx HTTPS.

Kartik and Piyush used normal hostname resolution. Their configured project DNS settings were also verified separately.

Nitin's `--resolve` request verifies HTTPS connectivity, hostname validation and certificate trust. It does not prove a default DNS lookup on Nitin's Mac.

## 6. Packet Evidence and Test Scope

The saved Wireshark capture subsequently verified the TCP handshake, TLS handshake, server certificate and encrypted application data.

That capture used a separate request forced to **TLS 1.2** so the server certificate could be inspected in the undecrypted capture. It is distinct from the TLS 1.3 requests recorded here.

No browser test is claimed by this document.

## 7. HTTP Status Clarification

The curl handshake prefix `(304)` is a TLS trace label, not an HTTP `304 Not Modified` response.

The requests recorded here returned **HTTP 200 OK**. Conditional HTTP caching was tested separately.

## 8. Related Evidence

- [Default Client DNS Verification](13_default_dns_verified.md)
- [TLS Certificate Metadata](19_tls_certificate_metadata.md)
- [Certificate Transfer Verification](21_certificate_transfer_verified.md)
- [Client Trust Commands](22_client_trust_commands.md)
- [Conditional HTTP Caching](24_https_cache_304_verified.md)
- [Verified DNS, TCP and TLS Packet Analysis](27_packet_analysis_verified.md)
- [Client Trust Instructions](../configs/TLS_Client_Trust.md)
