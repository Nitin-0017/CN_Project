# Phase 1 Evidence Checklist

Save actual evidence with member, command/action, timestamp and result. Remove secrets before sharing.

- LAN inventory for three Macs and ping results for all six directions.
- DNS resolution from Kartik and Piyush using Nitin's resolver.
- Both backend endpoints and X-Backend headers.
- Trusted HTTPS using the domain, without curl -k.
- Repeated requests showing both A and B via nginx.
- Cache-Control and cache hit or conditional 304.
- Saved DNS query/response, TCP handshake and TLS packet captures, with packet references.
- HTTP headers and source/destination ports.
- Wrong client DNS, wrong DNS record, one backend stopped, both stopped, wrong destination port.
- Restore confirmation after each failure.

Initial member-labelled hardware/default-route evidence saved in 01_network_inventory_initial.md. IPv4, mask, active MAC and peer ping evidence remain pending.

IPv4, subnet and active MAC evidence saved in 02_ipv4_inventory.md. Six directional peer ping results saved in 03_peer_ping_results.md; all passed with 0.0% packet loss.

Current network: hotspot inventory saved in 05_hotspot_inventory.md. Previous college-network tests are historical. Six new hotspot ping results and original screenshots are pending.

Backend startup outputs saved in 07_backend_startup.md. Kartik remote HTTP endpoint tests remain pending.

Four remote backend tests saved in 08_backend_http_tests.md; Task C complete. DNS setup is next.

DNS syntax validation and startup saved in 10_dns_startup.md. Remote app/api dig tests and system resolver setup remain pending.

Explicit DNS queries on Kartik and Piyush saved in 11_explicit_dns_queries.md. All four app/api tests passed. Default resolver setup remains pending.

Default/system DNS verification saved in 13_default_dns_verified.md, with originals Kartik_default_DNS.png and Piyush_default_DNS.jpg. Task B complete.

Successful six-request A/B round-robin repeat saved in 17_http_round_robin_verified.md. Initial failures are retained in 16_initial_http_load_balancing.md; cause unresolved.
