# Initial Network Inventory Evidence

Source: terminal outputs pasted by the user, labelled by member. Received 2026-10-03; execution timestamps were not provided. This is a transcription of relevant fields, not a complete original screenshot or terminal export.

Commands: networksetup -listallhardwareports; route -n get default.

| Member | Hardware Port | Device | Hardware Ethernet Address | Default Gateway | Default Route Interface | MTU |
|---|---|---|---|---|---|---|
| Nitin Kumar | Wi-Fi | en0 | 10:9f:41:c3:a3:65 | 10.7.0.1 | en0 | 1500 |
| Kartik Yadav | Wi-Fi | en0 | 10:9f:41:b8:66:4c | 10.7.0.1 | en0 | 1500 |
| Piyush Yadav | Wi-Fi | en0 | 10:9f:41:ba:cc:cc | 10.7.0.1 | en0 | 1500 |

All three default routes identify en0. Shared gateway is recorded; same-LAN peer connectivity is not yet proven. IPv4 and subnet mask are absent from these outputs. Hardware MAC addresses may differ from active Wi-Fi MAC addresses; confirm using ifconfig en0.
