# Phase 1 LAN Connectivity and Ping Checks

All three Macs were connected to the same hotspot LAN. Every machine pair was tested in both directions on 3 October 2026.

All six tests received four replies with zero packet loss.

## 1. Network Details

| Member | Private IP | Active Interface |
|---|---|---|
| Nitin | 10.63.169.3 | en0 |
| Kartik | 10.63.169.72 | en0 |
| Piyush | 10.63.169.63 | en0 |

- **Subnet:** 10.63.169.0/24
- **Subnet mask:** 255.255.255.0
- **Gateway:** 10.63.169.210

These are the addresses used during the recorded tests. Recheck them after reconnecting to the hotspot.

## 2. Nitin's Ping Tests

### Nitin → Kartik

```bash
ping -c 4 10.63.169.72
```

Recorded summary:

```text
4 packets transmitted, 4 packets received, 0.0% packet loss
round-trip min/avg/max/stddev = 8.167/48.869/92.322/33.066 ms
```

### Nitin → Piyush

```bash
ping -c 4 10.63.169.63
```

Recorded summary:

```text
4 packets transmitted, 4 packets received, 0.0% packet loss
round-trip min/avg/max/stddev = 5.152/87.109/328.553/139.406 ms
```

## 3. Kartik's Ping Tests

### Kartik → Nitin

```bash
ping -c 4 10.63.169.3
```

Recorded summary:

```text
4 packets transmitted, 4 packets received, 0.0% packet loss
round-trip min/avg/max/stddev = 6.516/18.868/53.218/19.840 ms
```

### Kartik → Piyush

```bash
ping -c 4 10.63.169.63
```

Recorded summary:

```text
4 packets transmitted, 4 packets received, 0.0% packet loss
round-trip min/avg/max/stddev = 13.736/44.545/102.520/36.211 ms
```

## 4. Piyush's Ping Tests

### Piyush → Nitin

```bash
ping -c 4 10.63.169.3
```

Recorded summary:

```text
4 packets transmitted, 4 packets received, 0.0% packet loss
round-trip min/avg/max/stddev = 5.251/36.134/110.632/43.330 ms
```

### Piyush → Kartik

```bash
ping -c 4 10.63.169.72
```

Recorded summary:

```text
4 packets transmitted, 4 packets received, 0.0% packet loss
round-trip min/avg/max/stddev = 5.067/37.986/77.628/30.989 ms
```

## 5. Results Summary

| Source | Destination | Replies | Packet Loss |
|---|---|---|---|
| Nitin | Kartik | 4/4 | 0.0% |
| Nitin | Piyush | 4/4 | 0.0% |
| Kartik | Nitin | 4/4 | 0.0% |
| Kartik | Piyush | 4/4 | 0.0% |
| Piyush | Nitin | 4/4 | 0.0% |
| Piyush | Kartik | 4/4 | 0.0% |

The tests confirmed bidirectional IP connectivity between every pair of project machines.

Ping uses ICMP Echo Request and Echo Reply. Successful ping establishes IP reachability; DNS resolution and application ports were verified separately.

## 6. Supporting Evidence

- [Hotspot Network Inventory](../evidence/05_hotspot_inventory.md)
- [Recorded Hotspot Ping Results](../evidence/06_hotspot_ping_results.md)

Earlier tests on the college network used different IP addresses. The results in this document belong to the hotspot network used for the final Phase 1 demonstration.
