# Phase 1 — Verified DNS, TCP and TLS Packet Analysis

## 1. Evidence Source

The original capture was analysed using Wireshark's `tshark` on **2026-10-03**.

[Original Capture — Phase1_DNS_TCP_TLS.pcapng](Phase1_DNS_TCP_TLS.pcapng)

The capture contains **41 packets**. The supplied Wireshark overview reported **0 dropped packets**.

Frame numbers and ports below refer to this saved capture. A new capture may use different frame numbers and ephemeral ports.

## 2. DNS Query and Response

### Verified Exchange — Frames 15 and 16

| Field | Recorded Value |
|---|---|
| Query frame | 15 |
| Response frame | 16 |
| Client IPv4 | 10.63.169.63 |
| Client UDP source port | 65089 |
| DNS server IPv4 | 10.63.169.3 |
| DNS server port | UDP 53 |
| Transaction ID | 0x9a52 |
| Queried name | app.teamcn.test |
| Query type | A |
| Returned IPv4 | 10.63.169.72 |
| Answer TTL | 60 seconds |
| Query-to-response time | Approximately 13.587 ms |

Query direction:

```text
10.63.169.63:65089 → 10.63.169.3:53
```

Response direction:

```text
10.63.169.3:53 → 10.63.169.63:65089
```

The response resolves the project hostname to Kartik's nginx address.

### Additional DNS Exchanges

| Frames | Query Type | Client UDP Source Port | Result |
|---|---|---:|---|
| 17 and 20 | A | 51906 | 10.63.169.72 |
| 18 and 19 | AAAA | 53386 | No IPv6 address answer |

The explicit dig exchange and subsequent curl lookup are separate exchanges; frame 15 should not be attributed to curl.

### DNS Screenshot

![DNS query and response evidence](Piyush_Wireshark_DNS.jpg)

## 3. TCP Three-Way Handshake

The HTTPS connection uses these endpoints:

```text
Client: 10.63.169.63:50050
Server: 10.63.169.72:8443
```

| Frame | Direction | Flags | Relative Sequence and Acknowledgement |
|---|---|---|---|
| 21 | Client → Server | SYN, ECE, CWR | Seq=0 |
| 22 | Server → Client | SYN, ACK, ECE | Seq=0, Ack=1 |
| 23 | Client → Server | ACK | Seq=1, Ack=1 |

The SYN starts the connection, the SYN-ACK acknowledges it, and the final ACK completes the handshake.

The additional ECE/CWR flags indicate ECN negotiation and do not invalidate the handshake.

TCP establishes a connection-oriented channel and provides reliable, ordered byte delivery. This capture shows connection establishment and acknowledgement progress; it is not a controlled packet-loss or retransmission experiment.

### TCP Screenshot

![TCP three-way handshake evidence](Piyush_Wireshark_TCP.jpg)

## 4. TLS Handshake

| Frame | Recorded TLS Messages |
|---|---|
| 24 | ClientHello with SNI app.teamcn.test |
| 27 | ServerHello, Certificate, Server Key Exchange and Server Hello Done |
| 29 | Client Key Exchange, Change Cipher Spec and encrypted handshake message |
| 31 | Server Change Cipher Spec and encrypted handshake message |
| 33 | Client encrypted Application Data |
| 35 | Server encrypted Application Data |

The ServerHello in frame 27 records version **0x0303**, identifying **TLS 1.2** for this handshake.

The corresponding supplied curl output reported the negotiated cipher:

```text
ECDHE-RSA-CHACHA20-POLY1305
```

This capture used a TLS 1.2 request. The separate ordinary HTTPS tests negotiated TLS 1.3.

### TLS Screenshot

![TLS handshake and encrypted application data](Piyush_Wireshark_TLS.jpg)

## 5. Server Certificate Verification

The public server certificate was extracted from frame **27** and saved as [server.crt](../configs/server.crt).

Its SHA-256 fingerprint matches the certificate fingerprints previously supplied by all three members:

```text
ED:D0:4D:21:98:8A:8C:84:B6:86:1B:76:31:9C:36:3B:71:7B:E5:B1:AD:7C:59:EE:5A:C6:E6:DC:1B:44:D4:C2
```

This confirms that the captured server certificate matches the distributed project certificate.

No private key was extracted or included.

## 6. Why HTTP Content Is Not Readable

Frames **33 and 35** contain encrypted TLS Application Data.

The HTTP headers and JSON body are encrypted inside the TLS records. They cannot be read directly from this capture without the required TLS decryption secrets.

HTTP response content and backend identifiers are established separately by the supplied curl evidence.

## 7. TCP Sequence and Acknowledgement Progress

| Data Frame | Recorded Sequence | Acknowledgement Frame | Recorded Acknowledgement |
|---|---:|---|---:|
| 33 — Client data | Seq=318 | 34 — Server ACK | Ack=432 |
| 35 — Server data | Seq=1344 | 36 — Client ACK | Ack=1606 |

These values show acknowledgement progress through the TCP byte stream.

The final RST/ACK in frame **41** follows encrypted alert and FIN/ACK traffic. That reset alone does not prove that the application request failed.

## 8. Verification Summary

The saved capture provides evidence of:

- Project DNS queries and responses with specific IPs, ports and answer records.
- The TCP SYN / SYN-ACK / ACK sequence.
- A TLS 1.2 handshake and the project server certificate.
- Encrypted application data after TLS negotiation.
- TCP sequence and acknowledgement progress.

Backend response content, load balancing, caching and failure recovery are documented separately.

## 9. Related Evidence

- [Capture Overview](26_packet_overview.md)
- [Packet Capture Guide](../docs/06_Packet_Capture.md)
- [TLS Certificate Metadata](19_tls_certificate_metadata.md)
- [Certificate Transfer Verification](21_certificate_transfer_verified.md)
- [HTTPS System Trust Verification](23_https_system_trust_verified.md)
- [Conditional HTTP Caching](24_https_cache_304_verified.md)
- [Failure Demonstration Results](../docs/07_Failure_Demonstrations.md)
