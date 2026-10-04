# Phase 1 Historical Updates

Earlier statuses below are historical snapshots and superseded by Progress.md.

# Phase 1 Progress

## Confirmed information

- Team members: Nitin Kumar, Kartik Yadav, Piyush Yadav.
- All laptops run macOS, as confirmed by the user.
- Scope is Phase 1 only.

## Task tracker

| Task | Owner | Status | Evidence |
|---|---|---|---|
| A LAN and topology | All; Nitin documents | Complete: Kartik hotspot inventory, topology and six peer pings | evidence/01_network_inventory_initial.md, evidence/02_ipv4_inventory.md, evidence/03_peer_ping_results.md |
| B Private DNS | Nitin; Kartik and Piyush clients | Complete: both clients configured, app/api dig and system resolution verified | evidence/09_dns_prerequisites.md, evidence/10_dns_startup.md and evidence/11_explicit_dns_queries.md |
| C Two backends | Nitin and Piyush | Complete: A/B startup, both endpoints and headers verified from Kartik | evidence/07_backend_startup.md and evidence/08_backend_http_tests.md |
| D nginx load balancing | Kartik | Complete: repeat HTTP domain test 6/6 passed A/B/A/B/A/B; initial timeout cause unknown | evidence/14_nginx_install_original.txt and evidence/15_nginx_validation_launch.md |
| E HTTPS and trust | Kartik; all clients | Trust and HTTPS complete on all three; TLS packet evidence pending Task G | evidence/19_tls_certificate_metadata.md |
| F HTTP caching | Piyush | Complete: HTTPS 200 from B, matching ETag conditional 304 from A | evidence/24_https_cache_304_verified.md |
| G Protocol capture | Piyush captures; Nitin documents; all explain | Complete: original pcapng verified DNS, TCP, TLS1.2 and encrypted application data | evidence/26_packet_overview.md and Piyush_DNS_TCP_TLS_overview.jpg |
| Five failure demonstrations | All | 4/5 complete: wrong DNS, wrong port, one/both backend failures and recovery; wrong-record pending | evidence/28_wrong_client_dns_failure.md |
| Configuration bundle and source | All | Pending | None yet |
| Phase 1 live checkpoint and viva | All | Pending | None yet |

## Update log

2026-10-03: Created Phase 1 role assignment, architecture draft and tracker. No LAN configuration or live test performed by the assistant.

2026-10-03: Recorded user-supplied hardware-port and default-route outputs for all three members. All report en0 and gateway 10.7.0.1. Hardware Wi-Fi MACs saved; active MAC confirmation pending. No peer connectivity inferred from shared gateway alone.

2026-10-03: Recorded all three IPv4 addresses, active MAC addresses and /19 subnet masks from user outputs. All interfaces report active. Computed common subnet 10.7.0.0/19. Peer connectivity is pending.

2026-10-03: All six user-supplied ping tests passed with 4 transmitted, 4 received and 0.0% loss. Task A LAN inventory/topology and reachability marked complete. DNS, HTTP and TLS remain untested.

2026-10-03: Recorded Homebrew and Python versions from all three members in evidence/04_tool_versions.md. User clarified private Wi-Fi has not been established; existing reachability remains verified but network ownership/control is unknown. Task A final acceptance awaits suitable project LAN confirmation. Screenshot guidance added.

## Next input

Piyush: check whether /Applications/Wireshark.app exists using ls -d /Applications/Wireshark.app. If absent, install Wireshark via Homebrew cask in next step. Capture client en0 DNS and HTTPS traffic from Piyush, whose default resolver is Nitin; save .pcapng and selected packet screenshots. All servers remain running.

2026-10-03 20:17 IST: HTTPS cache test passed with 200 B and conditional 304 A using identical ETag. Task F complete; cache-hit explanation and conditional behavior documented. Task G packet evidence and five failure demonstrations remain pending.

2026-10-03: Received and saved readable original caching screenshot as evidence/Piyush_HTTPS_cache_304.jpg; shows first 200 B, ETag/Cache-Control and conditional 304 A.

2026-10-03: Piyush Wireshark app installed and en0 capture screenshot received; displayed traffic is background and not sufficient project evidence. Fresh scoped capture instructions prepared in docs/06_Packet_Capture.md. Task G pending actual .pcapng and packet inspection.

2026-10-03 20:25 IST: DNS and TLS1.2 terminal test passed. Wireshark screenshot does not confirm fresh scoped capture. Task G remains pending actual project packets and .pcapng file. Capture UI troubleshooting next.

2026-10-03: Fresh stopped capture screenshot shows 41 packets, 0 dropped and project protocol flow. Saved screenshot and visible frame references 15-35. Await actual .pcapng and expanded DNS/TLS details; Task G partial.

2026-10-03: Original pcapng received, saved and analysed using tshark. Verified DNS ports, TCP handshake, TLS1.2/certificate and encrypted data. Public certificate extracted from frame27 and SHA256 matched. Task G complete; focused screenshots and five mandatory failure demonstrations next.

2026-10-03: Received original focused DNS/TCP/TLS screenshots and saved unchanged as JPEGs in evidence/. Packet evidence ready. Five failure demonstrations remain pending; first wrong-client-DNS test instructions added in docs/07_Failure_Demonstrations.md.

2026-10-03 20:47:10 IST: Piyush wrong-DNS test produced NXDOMAIN via 8.8.8.8 with successful 4/4 direct-IP ping. Saved original screenshot. Project DNS restore is next and remains unverified.

2026-10-03 20:48:14 IST: Wrong-client-DNS restoration verified and original screenshot saved. First failure demo complete. Next Piyush wrong destination port test on 8444, followed by correct8443 validation; all services remain running.

2026-10-03 20:51 IST: Wrong-port test complete: valid DNS, TCP8444 connection refused, correct8443 HTTP200 B. Saved original screenshot. One-backend-stop demonstration next, then restore A.

2026-10-03 20:54 IST: A stop screenshot and six B-only HTTPS HTTP200 results verified. Originals saved. A restart and A/B recovery verification required next.

2026-10-03 20:56:57-58 IST: Six recovery responses B/B/A/B/A/B all HTTP200. Saved recovery screenshot. Single-backend failure and recovery complete. Both-backend-stop test next; DNS/nginx must remain running.

2026-10-03 20:59 IST: Both-down test shows DNS NOERROR, trusted TLS1.3 and HTTP502. Saved screenshot and evidence. Restart both backends and verify A/B HTTP200 before next fault.

2026-10-03 21:02:35-36 IST: Both-backend recovery verified sixHTTP200 with B/B/A/B/A/B. Saved two originals. Only wrong-record failure demonstration remains; planned change app record to NitinIP with exact config backup/restoration.

2026-10-03: Nitin terminated old DNS with SIGTERM, backed up and changed only app record to wrong10.63.169.3. Syntax passed. Supplied restart output ends at password prompt; startup and failure test pending. Correct final config remains preserved in bundle separately from fault variant.

2026-10-03: New DNS process17542 active according to supplied query/reply logs. Piyush wrong-record lookup and HTTPS destination/error test next; restore still pending.

2026-10-03 21:16:30 IST: Wrong-record demo returned NOERROR A10.63.169.3 and curl tried that wrong IP with connection refused. Saved text evidence; restore correct DNS backup and verify HTTPS before marking last test complete.

2026-10-03: Correct DNS backup restored and syntax verified. PID21865 startup confirmed. Client cache flush, correct A answer and HTTPS200 verification pending to close final failure demonstration.
