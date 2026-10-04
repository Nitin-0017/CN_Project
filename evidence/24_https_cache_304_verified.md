# HTTPS Conditional Caching Verified

Source: Piyush terminal output supplied by user.

First request: https://app.teamcn.test:8443/api/cache. HTTP/1.1 200 OK, nginx/1.31.6, Date 2026-10-03 14:47:14 UTC = 20:17:14 IST, X-Backend B, Cache-Control public,max-age=60, Content-Type application/json; charset=utf-8, Content-Length 73.

ETag: "b80d47eec1d7c70fd74370ea406e78b8c98e4b022801f19211e18c548d169f61"

Body: {"project": "CN Phase 1", "resource": "shared-cache-demo", "version": 1}.

First headers/body saved on Piyush at ~/Documents/CN_Phase1/evidence/cache-first.headers and cache-first.json; these original files have not been transferred to assistant.

Conditional request supplied same ETag in If-None-Match. Response HTTP/1.1 304 Not Modified, X-Backend A, same Cache-Control and ETag, no JSON body shown. Date 2026-10-03 14:47:52 UTC = 20:17:52 IST.

Cross-backend validation works because /api/cache content and ETag are identical on A/B. This demonstrates conditional HTTP validation, not an automatic fresh browser cache hit. Task F complete using the permitted 304 demonstration. Original screenshot received, visually inspected and saved unchanged as Piyush_HTTPS_cache_304.jpg. Source attachment is JPEG, so its original format is preserved.
