# Phase 1 Client Packet Capture

Piyush's screenshot confirms Wireshark capturing en0. Background traffic shown; no project protocol-flow evidence verified yet.

Stop initial background capture. Open Capture Options, select en0 and apply this capture filter:

```text
(host 10.63.169.3 and port 53) or (host 10.63.169.72 and tcp port 8443)
```

Start a new capture; initial background capture may be discarded. Keep project servers running.

Piyush new terminal:

```sh
dig app.teamcn.test A
curl -v --tlsv1.2 --tls-max 1.2 --connect-timeout 5 --max-time 15 https://app.teamcn.test:8443/api/status
```

TLS 1.2 is supported in nginx configuration. Forcing this one request to TLS1.2 helps show server Certificate in an undecrypted capture; ordinary project TLS1.3 tests are already recorded. Certificate validation remains enabled. A dig query and following curl create evidence within the same capture; do not imply the explicit dig packet is necessarily the curl resolver's own query.

Stop capture after requests finish. Save as ~/Documents/CN_Phase1/evidence/Phase1_DNS_TCP_TLS.pcapng. Original file and selected packet screenshots required for final evidence. No capture file has been received or analysed yet.

Display filter for saved capture:

```text
dns || tcp.port == 8443
```

Next inspect DNS query/answer, identify TCP stream and SYN/SYN-ACK/ACK, TLS ClientHello/ServerHello/Certificate and encrypted application data. Record actual client ephemeral ports and frame numbers from supplied capture, never placeholders presented as results.
