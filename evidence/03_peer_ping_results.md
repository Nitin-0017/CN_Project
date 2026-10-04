# Phase 1 Peer Ping Evidence

Source: member-labelled terminal outputs supplied by the user on 2026-10-03. Execution timestamps not supplied. Summary transcribed from actual outputs.

| Source | Destination | Command | Sent | Received | Loss | RTT min/avg/max/stddev ms |
|---|---|---|---|---|---|---|
| Nitin | Kartik | ping -c 4 10.7.17.92 | 4 | 4 | 0.0% | 9.615/69.544/109.546/37.346 |
| Nitin | Piyush | ping -c 4 10.7.1.140 | 4 | 4 | 0.0% | 10.156/13.172/20.248/4.106 |
| Kartik | Nitin | ping -c 4 10.7.5.185 | 4 | 4 | 0.0% | 6.899/77.732/121.113/45.375 |
| Kartik | Piyush | ping -c 4 10.7.1.140 | 4 | 4 | 0.0% | 8.415/79.172/172.110/61.026 |
| Piyush | Nitin | ping -c 4 10.7.5.185 | 4 | 4 | 0.0% | 6.108/11.461/18.530/5.196 |
| Piyush | Kartik | ping -c 4 10.7.17.92 | 4 | 4 | 0.0% | 11.944/86.243/185.478/69.764 |

All six directions passed for this four-packet sample. This proves current ICMP peer reachability, not DNS, backend, HTTPS or other service-port availability.
