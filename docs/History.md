# Phase 1 Project History

This document records the main setup, testing and recovery milestones.

For the current project status, see [Progress](Progress.md). Historical IP addresses and process IDs must not be reused as current configuration values.

## 1. Initial Network Checks

The team first collected network information and ping results on the college network.

These outputs are retained as historical evidence. The final Phase 1 demonstration used Kartik's phone hotspot.

## 2. Final Hotspot Network

On 3 October 2026, all three Macs connected to the same hotspot LAN.

| Machine | Recorded IP |
|---|---|
| Nitin | 10.63.169.3 |
| Kartik | 10.63.169.72 |
| Piyush | 10.63.169.63 |

All machines used interface `en0`, subnet mask `255.255.255.0` and gateway `10.63.169.210`.

Six directional ping tests succeeded with four replies and zero packet loss each.

## 3. Backend Services

Nitin started Backend A on port `3001`. Piyush started Backend B on port `3002`.

Kartik tested `/` and `/api/status` on both backends. All four direct requests returned HTTP 200 and the correct backend identifiers.

## 4. Private DNS

Nitin installed and configured dnsmasq.

Both project domains were mapped to Kartik's edge IP:

```text
app.teamcn.test → 10.63.169.72
api.teamcn.test → 10.63.169.72
```

Kartik and Piyush verified direct DNS queries, configured their default Wi-Fi DNS to `10.63.169.3`, and confirmed successful resolution.

External forwarding was verified using example.com.

## 5. nginx HTTP Routing

Kartik configured nginx with Backend A and Backend B as upstream servers.

The initial HTTP test had four timeouts followed by successful responses. A later six-request test returned HTTP 200 for every request with alternating A/B responses.

The cause of the initial delay was not conclusively established.

## 6. TLS Certificate and HTTPS

Kartik generated a self-signed RSA 2048-bit certificate with SAN entries for both project domains.

nginx HTTPS was enabled on port `8443`.

An initial test using `--cacert` passed certificate verification and returned HTTP 200.

The public certificate was transferred to Nitin and Piyush. All three Macs reported identical SHA-256 fingerprints and installed explicit SSL trust.

Subsequent HTTPS tests on all three Macs passed certificate verification without `--cacert` or `--insecure`. Nitin used `--resolve`; Kartik and Piyush used their configured private DNS.

## 7. Conditional Caching

Piyush tested `/api/cache` through HTTPS.

| Time on 3 October 2026 | Result |
|---|---|
| 20:17:14 IST | HTTP 200 from Backend B with Cache-Control and ETag |
| 20:17:52 IST | HTTP 304 from Backend A after a matching If-None-Match request |

The matching ETag and bodyless 304 response verified conditional validation across both backends.

## 8. Wireshark Packet Capture

Piyush captured traffic on Wi-Fi interface `en0`.

The original `Phase1_DNS_TCP_TLS.pcapng` contains 41 packets. Wireshark reported zero dropped packets.

Analysis verified:

- DNS query and response in frames 15 and 16
- TCP SYN, SYN-ACK and ACK in frames 21–23
- TLS 1.2 handshake beginning in frame 24
- Server certificate in frame 27
- Encrypted Application Data in frames 33 and 35

Focused DNS, TCP and TLS screenshots were saved alongside the original capture.

## 9. Failure Demonstrations

### Wrong Client DNS

At 20:47:10 IST, Piyush's query through DNS server `8.8.8.8` returned NXDOMAIN. Ping to the edge IP still succeeded.

Private DNS was restored, and correct resolution was verified at 20:48:14 IST.

### Wrong Destination Port

At approximately 20:51 IST, a request to port `8444` was refused while DNS resolved correctly.

A request to the correct port `8443` returned HTTP 200.

### Backend A Stopped

With Backend A stopped, six HTTPS requests returned HTTP 200 from Backend B.

After recovery, the six-request sequence was:

```text
B, B, A, B, A, B
```

All responses returned HTTP 200.

### Both Backends Stopped

At 20:59:31 IST, DNS resolution and TLS verification succeeded, but nginx returned HTTP 502.

After backend recovery, six requests returned HTTP 200 with responses from both backends.

### Wrong DNS Record

Nitin temporarily changed the app record to `10.63.169.3`.

At 21:16:30 IST, Piyush received NOERROR with that incorrect IP. The HTTPS connection to the wrong machine was refused.

Nitin restored the working configuration and restarted dnsmasq.

At 21:21:22 IST, DNS returned the correct edge IP. At 21:21:29 IST, the HTTPS request returned HTTP 200 from Backend A.

## 10. Documentation Preparation

On 4 October 2026, the team prepared form answers and revised the setup and evidence documents around the completed tests.

Nitin also ran a fresh explicit public DNS query:

```bash
dig @8.8.8.8 app.teamcn.test A +time=3 +tries=1
```

At 10:57:41 IST, the query returned NXDOMAIN from `8.8.8.8`, providing the form's requested public DNS comparison.

## 11. Related Documents

- [Current Progress](Progress.md)
- [Architecture](Architecture.md)
- [Demo Guide](Demo_Guide.md)
- [Packet Capture](06_Packet_Capture.md)
- [Failure Demonstrations](07_Failure_Demonstrations.md)
- [Evidence Index](../evidence/INDEX.md)
