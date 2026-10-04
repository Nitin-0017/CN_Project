# Initial IPv4 Inventory — Historical Evidence

This document records the college-network IPv4 information collected before the team switched to Kartik's phone hotspot.

Use [Hotspot Inventory](05_hotspot_inventory.md) for the final Phase 1 network.

## 1. Evidence Source

The values were transcribed from member-labelled terminal outputs received on 3 October 2026.

Command execution timestamps were not supplied. This document summarises relevant fields rather than reproducing a complete terminal export.

## 2. Commands Used

```bash
ipconfig getifaddr en0
ifconfig en0
```

## 3. Recorded IPv4 and Interface Details

| Member | IPv4 Address | Active MAC Address | Interface | Status |
|---|---|---|---|---|
| Nitin Kumar | 10.7.5.185 | aa:ab:89:31:85:39 | en0 | active |
| Kartik Yadav | 10.7.17.92 | 1a:fb:f6:75:2f:39 | en0 | active |
| Piyush Yadav | 10.7.1.140 | 12:ba:93:33:97:2d | en0 | active |

## 4. Initial Network Details

| Property | Recorded or Calculated Value |
|---|---|
| MTU | 1500 |
| Netmask from ifconfig | 0xffffe000 |
| Dotted-decimal subnet mask | 255.255.224.0 |
| Prefix length | /19 |
| Calculated subnet | 10.7.0.0/19 |
| Broadcast address | 10.7.31.255 |
| Gateway from earlier route output | 10.7.0.1 |

All three recorded IPv4 addresses belong to the calculated subnet `10.7.0.0/19`.

## 5. Interpretation

The outputs establish the assigned IPv4 addresses, active interface status and subnet membership at the time of collection.

Subnet membership alone does not prove peer reachability. The subsequent initial-network ping results are recorded in [Peer Ping Results](03_peer_ping_results.md).

The active MAC addresses differ from the hardware addresses recorded earlier. The outputs do not establish the exact reason for that difference.

## 6. Final Project Network

The final demonstration used the hotspot subnet `10.63.169.0/24`, with different IP and active MAC addresses.

See:

- [Final Hotspot Inventory](05_hotspot_inventory.md)
- [Final Hotspot Ping Results](06_hotspot_ping_results.md)
- [Architecture](../docs/Architecture.md)
