# Phase 1 Backend Launch

Uses Python 3.12 or later and standard library only. Both members use identical server.py.

Working directory on group Macs: ~/Documents/CN_Phase1/backend (created via Terminal).

Nitin: python3 server.py --backend A --port 3001
Piyush: python3 server.py --backend B --port 3002

Keep terminals open; Ctrl C stops a backend. Allow incoming Python connections if macOS asks.

Kartik checks initial backend reachability:

```sh
curl -i --connect-timeout 5 http://10.63.169.3:3001/
curl -i --connect-timeout 5 http://10.63.169.3:3001/api/status
curl -i --connect-timeout 5 http://10.63.169.63:3002/
curl -i --connect-timeout 5 http://10.63.169.63:3002/api/status
```

These direct IP tests verify upstreams during setup. Final client demo uses the domain via nginx HTTPS.

Expected: HTTP 200, X-Backend A or B, correct JSON. /api/cache has shared content, Cache-Control max-age=60 and ETag; sending matching If-None-Match returns 304. HEAD supported. Unknown paths return 404. User startup outputs confirm A on 0.0.0.0:3001 and B on 0.0.0.0:3002. Kartik verified both / and /api/status endpoints over LAN on A and B with HTTP 200 and correct identifiers.
