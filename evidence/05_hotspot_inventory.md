# Phase 1 — Hotspot Network Inventory

## 1. Evidence Source

This inventory summarizes member-labelled terminal outputs supplied on **2026-10-03** from the three macOS laptops connected to Kartik's phone hotspot.

Exact command execution timestamps were not supplied. Kartik's latest hotspot inventory was used instead of his earlier college-network output.

## 2. Commands Used

Each member ran:

```bash
route -n get default
ipconfig getifaddr en0
ifconfig en0
```

These commands record the default gateway, IPv4 address, active interface, subnet mask, broadcast address, MTU and active MAC address.

## 3. Network Inventory

| Member | IPv4 Address | Active MAC Address | Default Gateway | Interface | Subnet Mask |
|---|---|---|---|---|---|
| Nitin Kumar | 10.63.169.3 | 8a:b3:88:c7:5c:1b | 10.63.169.210 | en0 | 255.255.255.0 (/24) |
| Kartik Yadav | 10.63.169.72 | 56:27:c7:bc:05:43 | 10.63.169.210 | en0 | 255.255.255.0 (/24) |
| Piyush Yadav | 10.63.169.63 | a2:f5:ea:dd:94:4d | 10.63.169.210 | en0 | 255.255.255.0 (/24) |

## 4. Shared Network Properties

| Property | Recorded Value |
|---|---|
| Project network | Kartik's phone hotspot |
| Network address | 10.63.169.0/24 |
| Subnet mask | 255.255.255.0 |
| Hexadecimal netmask | 0xffffff00 |
| Broadcast address | 10.63.169.255 |
| Default gateway | 10.63.169.210 |
| Interface on all three Macs | en0 |
| Interface status | active |
| MTU | 1500 |

All three recorded IPv4 addresses belong to the same /24 subnet.

## 5. Service Assignments

| Member | Service | Address and Port |
|---|---|---|
| Nitin | Private DNS server | 10.63.169.3 — UDP/TCP 53 |
| Nitin | Backend A | 10.63.169.3:3001 |
| Kartik | nginx HTTP reverse proxy | 10.63.169.72:8080 |
| Kartik | nginx HTTPS reverse proxy | 10.63.169.72:8443 |
| Piyush | Backend B | 10.63.169.63:3002 |

The DNS records `app.teamcn.test` and `api.teamcn.test` point to Kartik's nginx address, **10.63.169.72**.

## 6. Connectivity Verification

The subsequent hotspot ping tests passed in all six directions, with **4 requests sent, 4 replies received and 0.0% packet loss** in each sample.

Detailed results are recorded in [Hotspot Ping Results](06_hotspot_ping_results.md).

The inventory records addressing information; the separate ping tests demonstrate peer reachability at the time of testing.

## 7. Evidence Format and Network Changes

This file is a summary transcribed from supplied terminal outputs. Original inventory screenshots are not linked here.

Earlier college-network addresses in the `10.7.x.x` range remain historical evidence. The final Phase 1 setup uses the hotspot addresses recorded above.

Recheck the inventory before each demonstration. If DHCP assigns different addresses, update the DNS listener, DNS records, nginx upstreams and client DNS settings as applicable.

## 8. Related Documents

- [Hotspot Ping Results](06_hotspot_ping_results.md)
- [Project Architecture](../docs/Architecture.md)
- [DNS Setup](../configs/DNS_Setup.md)
- [nginx Setup](../configs/NGINX_Setup.md)
- [Live Demo Guide](../docs/Demo_Guide.md)
