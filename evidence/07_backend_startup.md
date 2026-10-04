# Phase 1 — Backend Startup Evidence

## 1. Evidence Source

This document records member-labelled terminal outputs supplied on **2026-10-03**. Exact command execution timestamps were not supplied.

Both members used the same [server.py](../backend/server.py), with different backend identifiers and listening ports.

The startup outputs below are terminal transcriptions. Original startup screenshots are not linked here.

## 2. Backend Assignments

| Member | Backend | Host IPv4 | Listening Port |
|---|---|---|---|
| Nitin Kumar | A | 10.63.169.3 | TCP 3001 |
| Piyush Yadav | B | 10.63.169.63 | TCP 3002 |

Working directory on both Macs:

```text
~/Documents/CN_Phase1/backend
```

## 3. Backend A — Nitin Kumar

### Launch Command

```bash
python3 server.py --backend A --port 3001
```

### Recorded Startup Output

```text
Backend A listening on 0.0.0.0:3001
```

Backend A listens on port **3001** across the host's IPv4 interfaces. Its project LAN address is:

```text
http://10.63.169.3:3001
```

## 4. Backend B — Piyush Yadav

### Launch Command

```bash
python3 server.py --backend B --port 3002
```

### Recorded Startup Output

```text
Backend B listening on 0.0.0.0:3002
```

Backend B listens on port **3002** across the host's IPv4 interfaces. Its project LAN address is:

```text
http://10.63.169.63:3002
```

## 5. Interpretation and Subsequent Verification

Both startup messages confirm that the servers successfully bound to their configured addresses and ports at launch.

`0.0.0.0` is the listening address; clients use the corresponding host's LAN IPv4 address to connect.

Startup messages alone do not establish remote reachability or correct HTTP responses. Subsequent tests from Kartik verified `/` and `/api/status` on both backends, with **HTTP 200** responses and the correct **X-Backend: A** or **X-Backend: B** identifiers.

Those results are recorded in [Backend HTTP Tests](08_backend_http_tests.md).

## 6. Running and Stopping the Backends

Keep each backend's terminal open while performing the project tests.

To stop a backend, press **Ctrl+C** in its own terminal. Restart it using the corresponding launch command above.

For a new demonstration, confirm that the backends are running and recheck their current LAN addresses.

## 7. Related Evidence

- [Backend Launch Instructions](../backend/README.md)
- [Backend Source Code](../backend/server.py)
- [Hotspot Network Inventory](05_hotspot_inventory.md)
- [Backend HTTP Tests](08_backend_http_tests.md)
- [HTTP Round-Robin Verification](17_http_round_robin_verified.md)
- [Single Backend Failure and Recovery](30_single_backend_failover.md)
- [Both Backends Down and Recovery](31_both_backends_down.md)
