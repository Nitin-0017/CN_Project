# Original Packet Capture Verification

Analysed original Phase1_DNS_TCP_TLS.pcapng with installed Wireshark tshark, 2026-10-03. Original saved unchanged in evidence/.

DNS frames 15/16: Piyush 10.63.169.63 UDP source 65089 to Nitin 10.63.169.3 UDP 53; app.teamcn.test A answer 10.63.169.72. Additional A frames 17/20 use client UDP source 51906, and AAAA frames 18/19 use 53386.

TCP frames 21/22/23: client 10.63.169.63:50050 -> edge 10.63.169.72:8443 SYN; reverse SYN-ACK; client ACK. SYN includes ECN ECE/CWR and SYN-ACK includes ECE, which does not invalidate the handshake.

TLS frame 24 ClientHello SNI app.teamcn.test; frame 27 ServerHello (version 0x0303 = TLS1.2), Certificate, Server Key Exchange and Server Hello Done. Frame 29 Client Key Exchange/Change Cipher Spec/encrypted handshake; frame 31 server Change Cipher Spec/encrypted handshake. Frames 33/35 contain encrypted client/server application data. HTTP headers/JSON are not visible without TLS decryption and are established separately by curl evidence.

Extracted public certificate from frame 27 into configs/server.crt. SHA-256 matches all three previously supplied fingerprints: ED:D0:4D:21:98:8A:8C:84:B6:86:1B:76:31:9C:36:3B:71:7B:E5:B1:AD:7C:59:EE:5A:C6:E6:DC:1B:44:D4:C2. No private key extracted or received.

TCP sequence/ack example: frame 33 client Seq=318 and server acknowledgement in frame 34 Ack=432; frame 35 server Seq=1344 and client acknowledgement in frame 36 Ack=1606. Demonstrates byte sequence/ack progress, not a retransmission or packet-loss experiment. Final RST/ACK frame 41 follows encrypted alert and FIN/ACK; it alone is not proof that the application request failed.

Task G protocol capture requirements verified with original packet file and separate HTTP/load-balancing evidence. Focused display screenshots improve demo presentation but do not replace original capture. Failure demonstrations remain outstanding.

Focused screenshot originals received and saved: Piyush_Wireshark_DNS.jpg (answer IP and DNS UDP ports), Piyush_Wireshark_TCP.jpg (three-way handshake and source/destination ports), Piyush_Wireshark_TLS.jpg (TLS1.2 certificate record and encrypted data list).
