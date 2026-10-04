# Initial College Network — Peer Ping Results

## 1. Evidence Source

These results summarize member-labelled terminal outputs supplied on **2026-10-03**. Command execution timestamps were not supplied.

This file records tests on the initial college network. Final project hotspot tests are documented separately in [Hotspot Ping Results](06_hotspot_ping_results.md).

## 2. Initial Network Addresses

| Member | IPv4 Address |
|---|---|
| Nitin Kumar | 10.7.5.185 |
| Kartik Yadav | 10.7.17.92 |
| Piyush Yadav | 10.7.1.140 |

Related network details are recorded in [Initial IPv4 Inventory](02_ipv4_inventory.md).

## 3. Test Method

Each member sent four ICMP Echo Requests to each of the other two members:

```bash
ping -c 4 <destination-ip>
```

The results below preserve the recorded packet counts, packet loss and round-trip times.

## 4. Ping Results

All RTT values are in **milliseconds**.

| Source | Destination | Command | Sent | Received | Packet Loss | RTT Min | RTT Avg | RTT Max | RTT Stddev |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|
| Nitin | Kartik | `ping -c 4 10.7.17.92` | 4 | 4 | 0.0% | 9.615 | 69.544 | 109.546 | 37.346 |
| Nitin | Piyush | `ping -c 4 10.7.1.140` | 4 | 4 | 0.0% | 10.156 | 13.172 | 20.248 | 4.106 |
| Kartik | Nitin | `ping -c 4 10.7.5.185` | 4 | 4 | 0.0% | 6.899 | 77.732 | 121.113 | 45.375 |
| Kartik | Piyush | `ping -c 4 10.7.1.140` | 4 | 4 | 0.0% | 8.415 | 79.172 | 172.110 | 61.026 |
| Piyush | Nitin | `ping -c 4 10.7.5.185` | 4 | 4 | 0.0% | 6.108 | 11.461 | 18.530 | 5.196 |
| Piyush | Kartik | `ping -c 4 10.7.17.92` | 4 | 4 | 0.0% | 11.944 | 86.243 | 185.478 | 69.764 |

## 5. Interpretation

All six directions received **4 replies from 4 requests**, with **0.0% packet loss** in each sample.

These results demonstrate bidirectional ICMP reachability between the three laptops at the time of testing. Ping alone does not verify DNS resolution, backend availability, TCP service ports or HTTPS certificate validation.

## 6. Final Project Network

The project later moved to Kartik's phone hotspot, using addresses in **10.63.169.0/24**. The college-network results above remain historical evidence and should not be used to validate the final hotspot setup.

Use these records for the final project network:

- [Final Hotspot Inventory](05_hotspot_inventory.md)
- [Final Hotspot Ping Results](06_hotspot_ping_results.md)
- [Project Ping Checks](../docs/03_Ping_Checks.md)
