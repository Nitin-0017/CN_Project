# Phase 1 Evidence

This folder contains recorded terminal outputs, original screenshots and the saved Wireshark capture from the Phase 1 tests.

The implementation tests and five failure demonstrations were completed on 3 October 2026.

## 1. Start Here

Open the [Evidence Index](INDEX.md) for direct links to each evidence file.

For explanations of the setup and results, see:

- [Architecture](../docs/Architecture.md)
- [Project Status](../docs/Progress.md)
- [Demo Guide](../docs/Demo_Guide.md)

## 2. Verified Evidence Checklist

- [x] Network inventory for all three Macs
- [x] Six directional hotspot ping tests
- [x] Private DNS resolution from Kartik and Piyush
- [x] Default client DNS configuration
- [x] Both backend services and endpoint responses
- [x] X-Backend identifiers
- [x] nginx reverse proxy and load balancing
- [x] HTTPS certificate verification on all three Macs
- [x] Cache-Control and ETag headers
- [x] Conditional HTTP 304 response
- [x] Original DNS, TCP and TLS packet capture
- [x] Focused Wireshark screenshots
- [x] Five failure scenarios and successful recovery

Demonstration video completion and faculty evaluation are tracked separately in [Project Status](../docs/Progress.md).

## 3. Evidence Types

### Terminal Records

Markdown and text files document the commands and results supplied during testing.

Some records contain selected output or summaries. They should not be described as original screenshots or complete raw logs unless their contents establish that.

### Screenshots

PNG and JPG files preserve the supplied visual evidence. They are linked from the related setup and test documents.

### Packet Capture

[Phase1_DNS_TCP_TLS.pcapng](Phase1_DNS_TCP_TLS.pcapng) is the original saved capture.

It contains 41 packets, with zero dropped packets reported by Wireshark. Detailed verification is recorded in [Packet Analysis](27_packet_analysis_verified.md).

## 4. Final Network Evidence

The recorded final network used Kartik's phone hotspot:

| Machine | IP Address |
|---|---|
| Nitin | 10.63.169.3 |
| Kartik | 10.63.169.72 |
| Piyush | 10.63.169.63 |

Use these files for the final LAN:

- [Hotspot Inventory](05_hotspot_inventory.md)
- [Hotspot Ping Results](06_hotspot_ping_results.md)

All six directional ping tests received four replies with zero packet loss.

## 5. DNS Evidence

- [DNS Startup](10_dns_startup.md)
- [Direct DNS Queries](11_explicit_dns_queries.md)
- [Original Settings and Forwarding](12_original_dns_and_forwarding.md)
- [Default Client DNS Verification](13_default_dns_verified.md)
- [Kartik DNS Screenshot](Kartik_default_DNS.png)
- [Piyush DNS Screenshot](Piyush_default_DNS.jpg)

Both project domains resolved to the nginx edge IP through Nitin's private DNS server.

## 6. Backend and nginx Evidence

- [Backend Startup](07_backend_startup.md)
- [Backend Endpoint Tests](08_backend_http_tests.md)
- [nginx Validation and Launch](15_nginx_validation_launch.md)
- [Successful HTTP Load Balancing](17_http_round_robin_verified.md)

Initial HTTP timeouts and related observations are retained separately:

- [Initial HTTP Test](16_initial_http_load_balancing.md)
- [Log Findings](18_log_findings.md)

A later repeat succeeded, but the initial delay's cause was not conclusively established.

## 7. HTTPS and Caching Evidence

- [Certificate Metadata](19_tls_certificate_metadata.md)
- [Initial Certificate Verification](20_https_cacert_verified.md)
- [Certificate Fingerprint Verification](21_certificate_transfer_verified.md)
- [Client Trust Commands](22_client_trust_commands.md)
- [Final HTTPS Trust Verification](23_https_system_trust_verified.md)
- [Conditional Cache Validation](24_https_cache_304_verified.md)
- [Caching Screenshot](Piyush_HTTPS_cache_304.jpg)

Final HTTPS tests passed certificate verification on all three Macs.

The caching test returned HTTP 200 from Backend B followed by a matching conditional HTTP 304 from Backend A. This demonstrates conditional validation, not an nginx proxy-cache hit.

## 8. Packet Evidence

- [Original Capture](Phase1_DNS_TCP_TLS.pcapng)
- [Verified Analysis](27_packet_analysis_verified.md)
- [Capture Overview](Piyush_DNS_TCP_TLS_overview.jpg)
- [DNS Screenshot](Piyush_Wireshark_DNS.jpg)
- [TCP Screenshot](Piyush_Wireshark_TCP.jpg)
- [TLS Screenshot](Piyush_Wireshark_TLS.jpg)

The capture demonstrates private DNS resolution, TCP connection establishment and TLS 1.2 negotiation followed by encrypted Application Data.

## 9. Failure and Recovery Evidence

| Scenario | Record |
|---|---|
| Wrong client DNS | [Failure and Recovery](28_wrong_client_dns_failure.md) |
| Wrong destination port | [Failure and Recovery](29_wrong_port_failure.md) |
| Backend A stopped | [Failover and Recovery](30_single_backend_failover.md) |
| Both backends stopped | [HTTP 502 and Recovery](31_both_backends_down.md) |
| Wrong DNS record | [Setup](32_wrong_record_setup.md), [Failure and Recovery](33_wrong_record_failure.md) |

All five scenarios were followed by successful restoration.

Wrong-record failure and recovery are supported by terminal text; a screenshot is not claimed.

## 10. Historical Evidence

The initial college-network records are retained for the setup history:

- [Initial Network Inventory](01_network_inventory_initial.md)
- [Initial IPv4 Inventory](02_ipv4_inventory.md)
- [Earlier Peer Pings](03_peer_ping_results.md)

These records use a different network and should not be substituted for the final hotspot inventory.

## 11. Evidence Interpretation

Recorded results establish behaviour at the time of testing. They do not imply that services remain running after terminals are closed.

Recheck IP addresses and restart the required services before a new live demonstration.

The repository contains the public certificate. The private server key remains on Kartik's Mac.
