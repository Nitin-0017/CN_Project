# Phase 1 Screenshot Guide

Each member should keep a local CN_Phase1_Evidence folder, with subfolders Nitin, Kartik and Piyush. Upload or share original screenshots to add them to the submission bundle; pasted text is recorded separately and is not described as a screenshot.

On macOS, Shift Command 4 selects a region. Capture readable command text, target address, relevant output and summary; exclude unrelated personal data. Keep the original capture and name it clearly.

## LAN evidence

For the final chosen project Wi-Fi, each member captures:

1. NAME_01_network_inventory.png: outputs of route -n get default, ipconfig getifaddr en0, and ifconfig en0. Use multiple images if needed for legibility.
2. NAME_02_ping_TARGET.png: the first assigned ping, including 4-packet summary.
3. NAME_03_ping_TARGET.png: the second assigned ping, including summary.
4. NAME_04_tool_versions.png: brew --version and python3 --version.

A network change invalidates old IPs for new configuration. Preserve prior evidence as initial-network tests and collect new inventory/ping screenshots on the chosen LAN. Never capture Wi-Fi passwords.

## Later evidence

DNS: dig output including question, answer and SERVER resolver. Backends: launch output and GET /, GET /api/status with X-Backend. nginx: validation and repeated A/B responses. HTTPS: domain URL and successful certificate validation. Caching: Cache-Control and actual 304/cache-hit result. Packet analysis: saved pcap/pcapng plus screenshots of DNS/TCP/TLS packets and port fields. Failures: fault description, resulting output and successful restore output.

Detailed capture instructions will be given at each corresponding setup/test step. Terminal outputs alone do not replace saved packet captures.
