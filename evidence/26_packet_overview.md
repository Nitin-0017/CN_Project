# Client Protocol Flow Screenshot

Source: stopped Wireshark screenshot supplied by user, received 2026-10-03. Original saved as Piyush_DNS_TCP_TLS_overview.jpg. 41 packets displayed and 0 dropped reported. Screenshot shows temporary capture name wireshark_Wi-FiYCRYW3.pcapng; final saved capture not yet supplied.

Visible project frame observations, pending original capture inspection:

| Frames | Observation |
|---|---|
| 15/16 | app.teamcn.test A query/answer, answer 10.63.169.72; transaction 0x9a52 |
| 17/20 | app.teamcn.test A query/answer, answer 10.63.169.72; transaction 0xe3dd |
| 18/19 | app.teamcn.test AAAA query/response, no IPv6 address displayed |
| 21 | Client 10.63.169.63:50050 to edge 10.63.169.72:8443 SYN (also ECE/CWR) |
| 22 | Edge 8443 to client 50050 SYN ACK (also ECE) |
| 23 | Client ACK, relative Seq=1 Ack=1 |
| 24 | ClientHello with SNI app.teamcn.test |
| 27 | ServerHello, Certificate, Server Key Exchange, Server Hello Done |
| 29 | Client Key Exchange, Change Cipher Spec, Encrypted Handshake Message |
| 31 | Server Change Cipher Spec, Encrypted Handshake Message |
| 33/35 | Application Data client/server, encrypted TLS records |

Capture includes unrelated DNS requests because filter includes all port53 traffic to Nitin. Those are not project evidence. Display filtering can hide them without changing original capture.

Client ephemeral TCP port 50050 and server destination 8443 are visible. Actual DNS source port, certificate fields and precise TLS version require expanding packet details or original .pcapng analysis. No invented values recorded. DNS query sequence preceding curl connection is consistent with request flow; confirm exact timing/lookup association from original file before stronger claims.
