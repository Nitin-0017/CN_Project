# Phase 1 Viva Notes

Every member should explain the whole system, not just assigned services.

| Question | Answer to understand |
|---|---|
| Request ka flow? | Client DNS se edgeIP leta hai, TCP connects, TLS validates/encrypts, HTTP reaches nginx, nginx A/B ko forwards, response returns. |
| DNS kya karta hai? | Domain ko IP se maps; application response nahi deta. Wrong resolver NXDOMAIN; wrong record successful lookup but wrong destination. |
| Port vs IP? | IP identifies host/interface; port identifies service.8444 refused while8443 worked. Client ports temporary; capture TCP50050 and DNS65089. |
| TCP handshake? | SYN, SYNACK, ACK establishes connection. Capture21-23. Seq/ACK track bytes; window advertises receiver capacity. |
| TCP reliability evidence? | Capture33 clientSeq318, frame34 ACK432; server35 Seq1344, frame36 ACK1606. Explain acknowledgements/retransmission concept; do not claim captured retransmissions. |
| HTTPS vs HTTP? | HTTP protected by TLS; nginx terminates TLS and sends plain HTTP to LAN backends. Client capture payload encrypted. |
| Certificate validation? | Trust anchor/explicit certificate trust plus validity and matching SAN. Fingerprint transfer comparison prevents accidental wrong cert. Self-signed requires explicit client trust. |
| TLS1.2 vs1.3? | Normal tests negotiated1.3; one request forced1.2 for visible certificate capture. TLS1.3 encrypts later handshake messages, so raw capture visibility differs. |
| Why reverse proxy? | Single client entry point; upstream addresses hidden from client URL; central TLS and routing. |
| Load balancing? | nginx default round-robin distributes acrossA/B. Passive failure detection/retry avoids unavailable backend; recovery may wait fail_timeout. |
| One/both backend failure? | One stops: other serves200. Both stop: DNS/TLS still work, nginx502. Edge itself is a single point of failure. |
| Cache-Control/ETag/304? | max-age60 permits freshness for60s; ETag validates representation; matching If-None-Match returns304 without body. curl conditional request is not automatic browser caching. |
| Same ETag across backends? | Shared /api/cache resource is identical onA/B, so conditional validation survives routing change. |
| Protocol layers? | DNS/HTTP application; TCP/UDP transport; IP network; Wi-Fi/Ethernet link. TLS sits above TCP; discuss course OSI session/presentation mapping. |
| HTTP versions? | HTTP1.1 demonstrated. HTTP2 only if supported/configured; HTTP3 explanation-only. No HTTP2 claim from h2 offered: server acceptedhttp/1.1. |
| CDN/cloud equivalents? | DNS like managedDNS, nginx like load balancer/edge, A/B like app instances. Running project remains local. CDN distributes/cache content near clients. |
| Email protocols? | SMTP sends; IMAP synchronises mailbox; POP3 downloads. Explanation-only in brief; not implemented. |

Practical diagnosis: DNS lookup first, then destination IP/port and TCP, then TLS trust/name/date, then HTTP status/upstream. Explain actual observations before guessing cause.
