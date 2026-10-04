# Phase 1 Final Status

Team: Nitin Kumar, Kartik Yadav, Piyush Yadav. Updated 2026-10-03 21:21 IST. Phase 1 only.

| Requirement | Status | Evidence |
|---|---|---|
| A private LAN, inventory and topology | Verified on Kartik hotspot | Architecture.md, evidence/05 and06 |
| B private DNS, two configured clients | Verified Kartik/Piyush normal lookup | evidence/13 and DNS screenshots |
| C both backend endpoints and identifiers | Verified from Kartik | evidence/07 and08, backend/server.py |
| D reverse proxy and round-robin | Verified HTTP/HTTPS A/B responses | evidence/17,30,31 |
| E TLS and client trust | Verified on all three, no bypass | evidence/19-23 and27 |
| F conditional HTTP caching | Verified200 B then304 A | evidence/24 and caching screenshot |
| G DNS/TCP/TLS packet evidence | Original capture analysed | Phase1_DNS_TCP_TLS.pcapng, evidence/27 and focused screenshots |
| Five controlled failures and recovery | All verified | evidence/28-33 |
| Architecture, configs, source, evidence bundle | Prepared | README.md and included folders |
| Faculty checkpoint and individual viva | To be presented by group | Demo_Guide.md and Viva_Notes.md |

## Current working setup

Nitin DNS10.63.169.3 and BackendA3001. Kartik nginx10.63.169.72 HTTPS8443, HTTP8080. Piyush BackendB10.63.169.63:3002. All on Kartik phone hotspot10.63.169.0/24, gateway10.63.169.210. Both app/api records restored to10.63.169.72.

## Remaining presentation work

Rehearse the live Phase1 checkpoint together and review viva notes. The submitted evidence has no browser screenshot; trusted curl meets the browser-or-curl route. Initial network inventory and ping evidence are text transcriptions; optional original screenshots can improve presentation. Wrong-record failure/recovery is supported by terminal text; screenshots can be added if available. No faculty evaluation result is claimed.

## Known observation

Initial HTTP test had four timeouts then recovered. Logs showed client-closed499 requests; cause not proven. Later repeated tests and failures/recoveries passed. This history is retained rather than claimed fixed by an unperformed change.
