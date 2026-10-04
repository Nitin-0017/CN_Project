# HTTPS HTTP Caching Test

Owner: Piyush. Keep all services running. Backend /api/cache has identical JSON and ETag on A/B so round-robin does not invalidate this shared-resource cache test.

Run in a new tab:

```sh
mkdir -p ~/Documents/CN_Phase1/evidence
curl -sS -D "$HOME/Documents/CN_Phase1/evidence/cache-first.headers" -o "$HOME/Documents/CN_Phase1/evidence/cache-first.json" --connect-timeout 5 --max-time 15 https://app.teamcn.test:8443/api/cache
cat ~/Documents/CN_Phase1/evidence/cache-first.headers
cat ~/Documents/CN_Phase1/evidence/cache-first.json
```

After confirming first response HTTP 200, Cache-Control public,max-age=60 and ETag:

```sh
CN_ETAG=$(awk 'tolower($1)=="etag:" {sub(/\r$/, "", $2); print $2; exit}' "$HOME/Documents/CN_Phase1/evidence/cache-first.headers")
printf 'ETag: %s\n' "$CN_ETAG"
curl -i --connect-timeout 5 --max-time 15 -H "If-None-Match: $CN_ETAG" https://app.teamcn.test:8443/api/cache
```

Do not send the conditional request if ETag is empty. Expected HTTP 304 Not Modified without a body, matching ETag and Cache-Control. curl does not automatically maintain a browser cache; this is explicit conditional validation, not a fresh browser cache hit. First full response is 200 with body, fresh cache can be reused during max-age, conditional validation sends a request and returns 304 when unchanged.

Capture initial 200 headers/content, actual ETag value, conditional command and 304 response. Named screenshot Piyush_HTTPS_cache_304.png. Share full outputs and optionally the saved header/JSON files. Verified from supplied Piyush output: first 200 B at 20:17:14 IST, conditional 304 A at 20:17:52 IST with matching ETag and no body. Original screenshot pending.
