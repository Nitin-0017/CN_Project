# Phase 1 DNS, TCP and TLS Packet Capture

We captured traffic on Piyush's Mac using Wireshark. The saved capture shows private DNS resolution, the TCP three-way handshake, and a TLS 1.2 handshake followed by encrypted application data.

## 1. Capture Setup

| Machine | Role | IP Address |
|---|---|---|
| Piyush | Client and packet capture | 10.63.169.63 |
| Nitin | Private DNS server | 10.63.169.3 |
| Kartik | nginx HTTPS edge server | 10.63.169.72 |

- **Network interface:** Wi-Fi `en0`
- **Capture file:** [Phase1_DNS_TCP_TLS.pcapng](../evidence/Phase1_DNS_TCP_TLS.pcapng)
- **Captured packets:** 41
- **Dropped packets reported by Wireshark:** 0

### Capture Filter

```text
(host 10.63.169.3 and port 53) or (host 10.63.169.72 and tcp port 8443)
```

### Commands Run on Piyush's Mac

```bash
dig app.teamcn.test A

curl -v --tlsv1.2 --tls-max 1.2 \
  --connect-timeout 5 --max-time 15 \
  https://app.teamcn.test:8443/api/status
```

TLS 1.2 was selected for this capture so the server certificate could be inspected without decrypting the session. Certificate validation remained enabled. Separate HTTPS tests successfully negotiated TLS 1.3.

The explicit `dig` command and the curl request were separate tests recorded in the same capture.

## 2. DNS Query and Response

### Display Filter

```text
dns.qry.name == "app.teamcn.test"
```

### Observed Packets

**Frame 15 — DNS query**

Piyush's client sent an A-record query for `app.teamcn.test`:

- Source: `10.63.169.63:65089`
- Destination: `10.63.169.3:53`
- Transport: UDP
- Transaction ID: `0x9a52`

**Frame 16 — DNS response**

Nitin's private DNS server returned the matching response:

- Source: `10.63.169.3:53`
- Destination: `10.63.169.63:65089`
- Answer: `app.teamcn.test → 10.63.169.72`
- Record type: A
- TTL: 60 seconds
- Response time: 13.587 milliseconds
- Result: No error

### What This Proves

A separate LAN client successfully queried our private DNS server and received the correct IP address of Kartik's nginx edge server.

### DNS Screenshot

![Private DNS query and response](../evidence/Piyush_Wireshark_DNS.jpg)

## 3. TCP Three-Way Handshake

### Display Filter

```text
frame.number >= 21 && frame.number <= 23
```

The filter `tcp.flags.syn == 1` shows the SYN and SYN-ACK packets, but the frame-number filter also includes the final ACK.

### Observed Packets

Sequence and acknowledgement numbers below are Wireshark relative values.

| Frame | Source | Destination | Flags | Sequence / Acknowledgement |
|---|---|---|---|---|
| 21 | 10.63.169.63:50050 | 10.63.169.72:8443 | SYN, ECE, CWR | Seq=0 |
| 22 | 10.63.169.72:8443 | 10.63.169.63:50050 | SYN, ACK, ECE | Seq=0, Ack=1 |
| 23 | 10.63.169.63:50050 | 10.63.169.72:8443 | ACK | Seq=1, Ack=1 |

### What This Proves

The client uses ephemeral source port `50050` to connect to nginx's HTTPS port `8443`.

The client sends SYN, the server replies with SYN-ACK, and the client completes the handshake with ACK. The TCP connection is established before the TLS Client Hello in frame 24.

TCP provides a connection-oriented, ordered byte stream. Sequence numbers, acknowledgements and retransmissions support reliable delivery. The ECE/CWR flags indicate ECN negotiation.

### TCP Screenshot

![TCP SYN SYN-ACK and ACK](../evidence/Piyush_Wireshark_TCP.jpg)

## 4. TLS Handshake

### Display Filter

```text
tls && tcp.port == 8443
```

### Observed Packets

| Frame | TLS Messages |
|---|---|
| 24 | Client Hello with SNI app.teamcn.test |
| 27 | Server Hello, Certificate, Server Key Exchange and Server Hello Done |
| 29 | Client Key Exchange, Change Cipher Spec and encrypted handshake message |
| 31 | Server Change Cipher Spec and encrypted handshake message |
| 33 | Encrypted client Application Data |
| 35 | Encrypted server Application Data |

### TLS Version and Certificate

The Server Hello negotiated **TLS 1.2**, represented by `0x0303`.

The corresponding curl output confirmed:

```text
SSL connection using TLSv1.2 / ECDHE-RSA-CHACHA20-POLY1305
SSL certificate verify ok.
```

The certificate contained:

- **Common Name:** `app.teamcn.test`
- **Subject Alternative Names:** `app.teamcn.test` and `api.teamcn.test`

The public certificate extracted from frame 27 matched the SHA-256 fingerprint verified on all three Macs.

### Why HTTP Content Is Not Readable

The HTTP request headers, response headers and JSON body are encrypted inside TLS Application Data records.

Without the TLS session secrets, Wireshark cannot display their plaintext. IP addresses, TCP ports and packet sizes remain visible.

Curl can display the HTTP response because it participates in the TLS session and decrypts the received data.

### TLS Screenshot

![TLS handshake certificate and encrypted application data](../evidence/Piyush_Wireshark_TLS.jpg)

## 5. Complete Capture Overview

![DNS TCP and TLS capture overview](../evidence/Piyush_DNS_TCP_TLS_overview.jpg)

The capture shows DNS resolution followed by TCP connection establishment, TLS negotiation and encrypted data exchange.

The corresponding curl request returned **HTTP 200 OK** with certificate verification enabled.

## 6. TCP Acknowledgement Evidence

The following packets show acknowledgement progress:

- Frame 33: client data with `Seq=318`.
- Frame 34: server acknowledgement with `Ack=432`.
- Frame 35: server data with `Seq=1344`.
- Frame 36: client acknowledgement with `Ack=1606`.

These observations demonstrate byte acknowledgement progress. They are not a packet-loss or retransmission experiment.

The final RST/ACK in frame 41 follows an encrypted alert and FIN/ACK. That packet alone does not prove that the application request failed.

## 7. Evidence Files

- [Original packet capture](../evidence/Phase1_DNS_TCP_TLS.pcapng)
- [DNS screenshot](../evidence/Piyush_Wireshark_DNS.jpg)
- [TCP screenshot](../evidence/Piyush_Wireshark_TCP.jpg)
- [TLS screenshot](../evidence/Piyush_Wireshark_TLS.jpg)
- [Capture overview](../evidence/Piyush_DNS_TCP_TLS_overview.jpg)
- [Detailed packet analysis](../evidence/27_packet_analysis_verified.md)
