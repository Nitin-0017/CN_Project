# Phase 1 Architecture Draft

Team: Nitin Kumar, Kartik Yadav, Piyush Yadav.
Chosen domain: app.teamcn.test and api.teamcn.test. The teamcn label is a project choice, not a faculty-assigned number. Both records point to Kartik 10.63.169.72.

## Network inventory

| Member | OS | IPv4 | Subnet mask | Gateway | Interface | MAC address |
|---|---|---|---|---|---|---|
| Nitin Kumar | macOS | 10.63.169.3 | 255.255.255.0 (/24) | 10.63.169.210 | en0 | 8a:b3:88:c7:5c:1b |
| Kartik Yadav | macOS | 10.63.169.72 | 255.255.255.0 (/24) | 10.63.169.210 | en0 | 56:27:c7:bc:05:43 |
| Piyush Yadav | macOS | 10.63.169.63 | 255.255.255.0 (/24) | 10.63.169.210 | en0 | a2:f5:ea:dd:94:4d |

## Services

| Host | Service | Port |
|---|---|---|
| Nitin | DNS | UDP/TCP 53 |
| Nitin | Backend A | TCP 3001 |
| Kartik | nginx HTTPS edge | TCP 8443 proposed |
| Piyush | Backend B | TCP 3002 |

## Request flow

Client on Kartik or Piyush → DNS query to Nitin → Kartik IPv4 returned → TCP connection to Kartik:8443 → TLS negotiation → HTTP request inside TLS → nginx forwards HTTP to Nitin:3001 or Piyush:3002 → response via nginx to client.

TLS terminates at nginx. Backend traffic is plain HTTP over the private LAN. DNS discovers the edge address; it does not carry the web request. nginx selects the backend without exposing backend selection to the client URL.

## Topology

All three laptops attach to the same Wi-Fi router or private LAN.

```text
Kartik/Piyush clients --- DNS ---> Nitin DNS
Kartik/Piyush clients --- HTTPS -> Kartik nginx
                                  |-- HTTP --> Nitin Backend A
                                  |-- HTTP --> Piyush Backend B
```

## Protocol layers

DNS and HTTP: application. TCP/UDP: transport. IP: network. Wi-Fi/Ethernet: link. TLS provides security above TCP; discuss the course's OSI mapping in viva.

## Verification

Latest hotspot inventory: all three Macs report en0 active, netmask 0xffffff00 = 255.255.255.0 (/24), broadcast 10.63.169.255, and gateway 10.63.169.210. All current IPv4 addresses belong to 10.63.169.0/24. All six hotspot peer pings passed with 0.0% loss. Kartik verified GET / and GET /api/status on both A and B with HTTP 200 and correct X-Backend headers. DNS records and default/system resolution verified on Kartik and Piyush. HTTP nginx domain routing and round-robin verified with six consecutive HTTP 200 responses A/B/A/B/A/B. Initial timeouts recovered on repeat; cause unknown. HTTPS on 8443 verified with TLS1.3 and trusted certificate on all three Macs. Kartik/Piyush use normal DNS; Nitin client test used --resolve. TLS terminates at nginx; upstream HTTP unchanged. Packet evidence remains pending. Earlier college-network pings remain historical evidence only. Recheck addresses after reconnection or DHCP changes.

## Project LAN suitability

Following the instruction to switch to a controlled phone hotspot, the group supplied matching new subnet/gateway inventories. These outputs establish addressing consistency; the user confirmed Kartik owns the phone hotspot and all six directional ping tests passed. Kartik's latest inventory block supersedes the older college-network blocks in the same pasted message.
