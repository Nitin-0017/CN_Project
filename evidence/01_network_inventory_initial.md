# Initial Network Inventory — Historical Evidence

This record describes the initial college-network setup before the team switched to Kartik's phone hotspot.

It is retained for project history. It is not the inventory of the final Phase 1 network.

## 1. Evidence Source

The information below was transcribed from member-labelled terminal outputs received on 3 October 2026.

Execution timestamps were not provided. This is a summary of relevant fields, not a complete terminal export or original screenshot.

## 2. Commands Used

```bash
networksetup -listallhardwareports
route -n get default
```

## 3. Recorded Initial Inventory

| Member | Hardware Port | Device | Hardware Ethernet Address | Default Gateway | Route Interface | MTU |
|---|---|---|---|---|---|---|
| Nitin Kumar | Wi-Fi | en0 | 10:9f:41:c3:a3:65 | 10.7.0.1 | en0 | 1500 |
| Kartik Yadav | Wi-Fi | en0 | 10:9f:41:b8:66:4c | 10.7.0.1 | en0 | 1500 |
| Piyush Yadav | Wi-Fi | en0 | 10:9f:41:ba:cc:cc | 10.7.0.1 | en0 | 1500 |

## 4. What These Outputs Establish

The initial outputs identified Wi-Fi device `en0` and a shared default gateway.

These outputs alone did not establish peer connectivity. IPv4 addresses and subnet masks were recorded separately, and ping tests were performed later.

Hardware Ethernet addresses reported by `networksetup` may differ from the active Wi-Fi addresses reported by `ifconfig`.

## 5. Final Project Network

The team subsequently switched to Kartik's phone hotspot.

Use the following records for the final Phase 1 setup:

- [Hotspot Network Inventory](05_hotspot_inventory.md)
- [Hotspot Ping Results](06_hotspot_ping_results.md)
- [Final Architecture](../docs/Architecture.md)

The final recorded hotspot gateway was `10.63.169.210`, with subnet `10.63.169.0/24`. All six directional hotspot ping tests passed with zero packet loss.
