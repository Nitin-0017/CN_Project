# Phase 1 Evidence Index

This index links the recorded terminal outputs, original screenshots and packet capture used to verify Phase 1.

The final setup used Kartik's phone hotspot. Earlier college-network outputs are retained separately as historical evidence.

## 1. LAN Inventory and Connectivity

| Evidence | File |
|---|---|
| Final hotspot network inventory | [Hotspot Inventory](05_hotspot_inventory.md) |
| Six directional ping tests | [Hotspot Ping Results](06_hotspot_ping_results.md) |
| Recorded tool versions | [Tool Versions](04_tool_versions.md) |

All six hotspot ping tests received four replies with zero packet loss.

## 2. Backend Services

| Evidence | File |
|---|---|
| Backend A and B startup | [Backend Startup](07_backend_startup.md) |
| Direct endpoint tests from Kartik | [Backend HTTP Tests](08_backend_http_tests.md) |
| Shared backend source | [server.py](../backend/server.py) |

Both backends returned HTTP 200 with the correct identifiers.

## 3. Private DNS

| Evidence | File |
|---|---|
| DNS prerequisites | [Prerequisites](09_dns_prerequisites.md) |
| dnsmasq startup | [DNS Startup](10_dns_startup.md) |
| Direct app and api queries | [Explicit DNS Queries](11_explicit_dns_queries.md) |
| Original client settings and forwarding | [Original DNS and Forwarding](12_original_dns_and_forwarding.md) |
| Default DNS on both clients | [Default DNS Verification](13_default_dns_verified.md) |
| Kartik screenshot | [Kartik DNS](Kartik_default_DNS.png) |
| Piyush screenshot | [Piyush DNS](Piyush_default_DNS.jpg) |

Both clients resolved the project domains to `10.63.169.72` using private DNS server `10.63.169.3`.

## 4. nginx and Load Balancing

| Evidence | File |
|---|---|
| Original installation output | [nginx Installation](14_nginx_install_original.txt) |
| Configuration validation and launch | [Validation and Launch](15_nginx_validation_launch.md) |
| Initial HTTP test with timeouts | [Initial HTTP Test](16_initial_http_load_balancing.md) |
| Initial test screenshot | [Initial HTTP Screenshot](Piyush_HTTP_load_balancing_initial.jpg) |
| Successful six-request HTTP repeat | [Round-Robin Verification](17_http_round_robin_verified.md) |
| Log observations | [Log Findings](18_log_findings.md) |
| Original logs and OpenSSL output | [Original Output](18_nginx_logs_openssl_original.txt) |

The successful HTTP repeat returned six HTTP 200 responses with alternating A/B identifiers. Initial timeouts are retained as recorded observations.

HTTPS recovery runs containing both backends are linked in the failure sections below.

## 5. TLS Certificate and Client Trust

| Evidence | File |
|---|---|
| Certificate metadata | [Certificate Details](19_tls_certificate_metadata.md) |
| Initial HTTPS test using --cacert | [Initial Certificate Verification](20_https_cacert_verified.md) |
| Initial HTTPS screenshot | [Kartik HTTPS Screenshot](Kartik_HTTPS_cacert_test.jpg) |
| Matching certificate fingerprints | [Certificate Transfer Verification](21_certificate_transfer_verified.md) |
| System keychain trust commands | [Client Trust Commands](22_client_trust_commands.md) |
| Final HTTPS tests on all three Macs | [System Trust Verification](23_https_system_trust_verified.md) |

The final HTTPS tests passed certificate verification without `--cacert` or `--insecure`. Nitin used `--resolve`; Kartik and Piyush used the configured private DNS.

## 6. HTTP Caching

| Evidence | File |
|---|---|
| HTTP 200 followed by conditional 304 | [Cache Validation](24_https_cache_304_verified.md) |
| Initial headers, ETag and 304 screenshot | [Caching Screenshot](Piyush_HTTPS_cache_304.jpg) |

The initial response came from Backend B. The matching conditional request returned HTTP 304 from Backend A without a response body.

## 7. Wireshark Packet Capture

| Evidence | File |
|---|---|
| Earlier capture attempt record | [Capture Attempt](25_tls12_capture_attempt.md) |
| Saved capture overview | [Packet Overview](26_packet_overview.md) |
| Verified packet analysis | [Detailed Analysis](27_packet_analysis_verified.md) |
| Original packet capture | [Phase1_DNS_TCP_TLS.pcapng](Phase1_DNS_TCP_TLS.pcapng) |
| Overview screenshot | [Capture Overview](Piyush_DNS_TCP_TLS_overview.jpg) |
| DNS screenshot | [DNS Query and Response](Piyush_Wireshark_DNS.jpg) |
| TCP screenshot | [TCP Three-Way Handshake](Piyush_Wireshark_TCP.jpg) |
| TLS screenshot | [TLS Handshake](Piyush_Wireshark_TLS.jpg) |

The original capture contains 41 packets, with zero dropped packets reported by Wireshark.

Verified frames:

- DNS: 15 and 16
- TCP three-way handshake: 21–23
- TLS Client Hello: 24
- Server Hello and Certificate: 27
- Encrypted Application Data: 33 and 35

## 8. Wrong Client DNS

| Evidence | File |
|---|---|
| Failure and recovery record | [Wrong Client DNS](28_wrong_client_dns_failure.md) |
| NXDOMAIN with successful IP ping | [Failure Screenshot](Piyush_failure_wrong_DNS.jpg) |
| Correct DNS restored | [Recovery Screenshot](Piyush_restore_DNS.jpg) |

## 9. Wrong Destination Port

| Evidence | File |
|---|---|
| Port 8444 failure and port 8443 recovery | [Wrong Port Test](29_wrong_port_failure.md) |
| Terminal screenshot | [Wrong Port Screenshot](Piyush_failure_wrong_port.jpg) |

## 10. Backend A Stopped

| Evidence | File |
|---|---|
| Single-backend failure and recovery | [Failover Record](30_single_backend_failover.md) |
| Nitin stops Backend A | [Backend A Stopped](Nitin_backend_A_stopped.png) |
| Six successful responses from B | [Failover Screenshot](Piyush_single_backend_failover.jpg) |
| Responses from both backends after recovery | [Recovery Screenshot](Piyush_backend_A_recovery.jpg) |

## 11. Both Backends Stopped

| Evidence | File |
|---|---|
| HTTP 502 and subsequent recovery | [Both Backends Down](31_both_backends_down.md) |
| DNS and TLS succeed, HTTP returns 502 | [Failure Screenshot](Kartik_both_backends_down.jpg) |
| Recovery responses — first image | [Recovery Screenshot 1](Kartik_both_backends_recovery_1.jpg) |
| Recovery responses — second image | [Recovery Screenshot 2](Kartik_both_backends_recovery_2.jpg) |

## 12. Wrong DNS Record IP

| Evidence | File |
|---|---|
| Incorrect record configuration | [Fault Setup](32_wrong_record_setup.md) |
| Wrong answer, connection refusal and recovery | [Failure and Recovery](33_wrong_record_failure.md) |

This scenario is supported by recorded terminal text. A screenshot is not claimed.

## 13. Historical College-Network Evidence

| Evidence | File |
|---|---|
| Initial network inventory | [Initial Inventory](01_network_inventory_initial.md) |
| Initial IPv4 details | [IPv4 Inventory](02_ipv4_inventory.md) |
| Earlier peer pings | [Initial Ping Results](03_peer_ping_results.md) |

These files describe the earlier network. Use the hotspot inventory and ping records for the final Phase 1 setup.

## 14. Related Documentation

- [Architecture](../docs/Architecture.md)
- [Project Status](../docs/Progress.md)
- [Demo Guide](../docs/Demo_Guide.md)
- [Caching Test](../docs/05_Caching_Test.md)
- [Packet Capture Analysis](../docs/06_Packet_Capture.md)
- [Failure Demonstrations](../docs/07_Failure_Demonstrations.md)

Terminal text records, screenshots and packet captures are separate evidence types. Image links refer to the saved original screenshots; the packet capture preserves the recorded packet data.
