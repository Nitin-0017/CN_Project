# IPv4 Inventory Evidence

Source: user-pasted, member-labelled outputs of ipconfig getifaddr en0 and ifconfig en0. Received 2026-10-03; command execution times not supplied.

| Member | IPv4 | Active ether address | Interface status |
|---|---|---|---|
| Nitin Kumar | 10.7.5.185 | aa:ab:89:31:85:39 | active |
| Kartik Yadav | 10.7.17.92 | 1a:fb:f6:75:2f:39 | active |
| Piyush Yadav | 10.7.1.140 | 12:ba:93:33:97:2d | active |

All three report en0, MTU 1500, netmask 0xffffe000 and broadcast 10.7.31.255. Netmask conversion is 255.255.224.0 = /19. Calculated network is 10.7.0.0/19 for all three addresses. Earlier default-route outputs give gateway 10.7.0.1.

Active MACs differ from the hardware addresses reported earlier. Record these active MACs for the current connection; the exact reason for the difference is not established by these outputs. Same subnet does not prove peer reachability. Ping results are pending.
