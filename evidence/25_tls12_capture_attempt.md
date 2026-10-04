# Phase 1 — Initial TLS 1.2 Capture Attempt

## 1. Evidence Source

This document records Piyush's supplied DNS and curl outputs from **2026-10-03**, along with the Wireshark observation made during the initial capture attempt.

It preserves the initial attempt. The subsequently saved project capture and verified packet analysis are linked below.

## 2. Recorded DNS Query

Command:

```bash
dig app.teamcn.test A
```

### Recorded Result

| Field | Value |
|---|---|
| Execution time (IST) | 2026-10-03 20:25:37 |
| Status | NOERROR |
| Queried name | app.teamcn.test |
| Answer type | A |
| Returned IPv4 address | 10.63.169.72 |
| TTL | 60 seconds |
| DNS server | 10.63.169.3#53 |
| Query time | 13 ms |
| Query ID | 17924 |

## 3. TLS 1.2 HTTPS Request

The supplied curl request used `--tlsv1.2 --tls-max 1.2` to restrict negotiation to TLS 1.2.

The equivalent request command is:

```bash
curl -v \
  --tlsv1.2 \
  --tls-max 1.2 \
  https://app.teamcn.test:8443/api/status
```

### Recorded Result

| Field | Value |
|---|---|
| Negotiated TLS version | TLSv1.2 |
| Reported cipher | ECDHE-RSA-CHACHA20-POLY1305 |
| HTTP protocol | HTTP/1.1 |
| Certificate and hostname verification | Passed |
| HTTP status | 200 OK |
| Backend identifier | A |
| Response Date (UTC) | 2026-10-03 14:55:48 |
| Equivalent time (IST) | 2026-10-03 20:25:48 |

Certificate verification remained enabled. No `-k` bypass flag was used.

## 4. Initial Wireshark Observation

The screenshot supplied at this stage displayed background IPv6 traffic on port 443 and mDNS packets.

That screenshot did not establish that a fresh capture containing the project DNS and HTTPS traffic had been collected or saved.

The successful terminal request demonstrated TLS connectivity, but its curl trace alone did not provide Wireshark packet evidence.

## 5. Subsequent Capture Completion

A focused project capture was subsequently supplied and analysed:

[Phase1_DNS_TCP_TLS.pcapng](Phase1_DNS_TCP_TLS.pcapng)

The final capture contains project DNS query/response packets, the TCP three-way handshake, TLS 1.2 handshake messages and encrypted application data.

Original focused screenshots are linked in [Verified Packet Analysis](27_packet_analysis_verified.md).

The earlier capture uncertainty is therefore historical; the completed packet evidence is documented separately.

## 6. Evidence Scope

The terminal timestamps and query ID in this file belong to the initial attempt. They should not be assumed to identify the packets in the final saved capture.

Use the final packet analysis for verified frame numbers, client ports and protocol details.

## 7. Related Documents

- [Packet Capture Overview](26_packet_overview.md)
- [Verified DNS, TCP and TLS Analysis](27_packet_analysis_verified.md)
- [Packet Capture Guide](../docs/06_Packet_Capture.md)
- [HTTPS System Trust Verification](23_https_system_trust_verified.md)
