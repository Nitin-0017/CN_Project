# Phase 1 — Hotspot Peer Ping Evidence

## 1. Evidence Source

These results summarize member-labelled terminal outputs supplied on **2026-10-03**.

All three Macs were connected to **Kartik's phone hotspot**. Exact command execution timestamps were not supplied.

This document records transcribed terminal results. Original ping screenshots are not linked here.

## 2. Network Details

| Member | IPv4 Address |
|---|---|
| Nitin Kumar | 10.63.169.3 |
| Kartik Yadav | 10.63.169.72 |
| Piyush Yadav | 10.63.169.63 |

- **Subnet:** 10.63.169.0/24
- **Subnet mask:** 255.255.255.0
- **Default gateway:** 10.63.169.210
- **Interface:** en0 on all three Macs

Full addressing details are recorded in [Hotspot Network Inventory](05_hotspot_inventory.md).

## 3. Test Method

Each member sent four ICMP Echo Requests to each of the other two members:

```bash
ping -c 4 <destination-ip>
```

This produced six directional tests, covering connectivity between every pair of laptops in both directions.

## 4. Recorded Results

All RTT values are in **milliseconds**.

| Source | Destination | Command | Sent | Received | Packet Loss | RTT Min | RTT Avg | RTT Max | RTT Stddev |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|
| Nitin | Kartik | `ping -c 4 10.63.169.72` | 4 | 4 | 0.0% | 8.167 | 48.869 | 92.322 | 33.066 |
| Nitin | Piyush | `ping -c 4 10.63.169.63` | 4 | 4 | 0.0% | 5.152 | 87.109 | 328.553 | 139.406 |
| Kartik | Nitin | `ping -c 4 10.63.169.3` | 4 | 4 | 0.0% | 6.516 | 18.868 | 53.218 | 19.840 |
| Kartik | Piyush | `ping -c 4 10.63.169.63` | 4 | 4 | 0.0% | 13.736 | 44.545 | 102.520 | 36.211 |
| Piyush | Nitin | `ping -c 4 10.63.169.3` | 4 | 4 | 0.0% | 5.251 | 36.134 | 110.632 | 43.330 |
| Piyush | Kartik | `ping -c 4 10.63.169.72` | 4 | 4 | 0.0% | 5.067 | 37.986 | 77.628 | 30.989 |

## 5. Interpretation

All six tests passed, with **4 replies received from 4 requests** and **0.0% packet loss** in each sample.

These results demonstrate bidirectional ICMP reachability between all three laptops on the project hotspot at the time of testing.

Round-trip times varied between requests. The recorded outputs do not establish the cause of this variation.

Ping alone does not verify DNS resolution, TCP service availability, HTTP responses or HTTPS certificate validation. Those functions were tested separately and are documented in the evidence linked below.

## 6. Related Service Evidence

- [Backend HTTP Tests](08_backend_http_tests.md)
- [Explicit DNS Queries](11_explicit_dns_queries.md)
- [Default Client DNS Verification](13_default_dns_verified.md)
- [HTTP Round-Robin Verification](17_http_round_robin_verified.md)
- [HTTPS System Trust Verification](23_https_system_trust_verified.md)
- [DNS, TCP and TLS Packet Analysis](27_packet_analysis_verified.md)

## 7. Network Scope

These are the ping results for the final Phase 1 hotspot setup.

Earlier college-network ping results are preserved separately in [Initial Peer Ping Results](03_peer_ping_results.md).

Recheck the laptops' IPv4 addresses after reconnecting to the hotspot, and repeat the tests if the addresses change.
