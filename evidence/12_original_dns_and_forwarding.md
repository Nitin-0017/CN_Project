# Original Client DNS Settings and Forwarding Tests

Source: user-supplied terminal outputs, 2026-10-03.

Kartik services: Thunderbolt Bridge, Wi-Fi. Wi-Fi getdnsservers returned: There aren't any DNS Servers set on Wi-Fi. This indicates no manually configured DNS entries; automatic network-supplied DNS remains applicable.

Piyush services: Thunderbolt Bridge, Wi-Fi, iPhone USB. Wi-Fi manual DNS entries, in order: 8.8.8.8, 4.2.2.2.

Both ran dig @10.63.169.3 example.com A +time=3 +tries=1 and received NOERROR with two A answers 172.66.147.243 and 104.20.23.154, SERVER 10.63.169.3#53.

| Client | Time IST | Query ms | TTL seconds | Query ID |
|---|---|---|---|---|
| Kartik | 2026-10-03 19:36:29 | 72 | 134 | 44220 |
| Piyush | 2026-10-03 19:36:39 | 24 | 124 | 58645 |

Forwarding via Nitin succeeded at these test times. Default DNS settings have not yet been changed or verified.
