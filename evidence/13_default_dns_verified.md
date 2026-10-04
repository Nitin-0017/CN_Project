# Default Client DNS Verification

User supplied terminal text and original images on 2026-10-03. Images copied unchanged as Kartik_default_DNS.png and Piyush_default_DNS.jpg. Both show configured DNS, app/api dig without explicit @ server, and macOS dscacheutil lookup.

Both executed sudo networksetup -setdnsservers "Wi-Fi" 10.63.169.3. Subsequent getdnsservers returned 10.63.169.3.

| Client | Query | Time IST | Query time ms | ID |
|---|---|---|---|---|
| Kartik | app.teamcn.test A | 2026-10-03 19:40:16 | 56 | 59756 |
| Kartik | api.teamcn.test A | 2026-10-03 19:40:34 | 18 | 23566 |
| Piyush | app.teamcn.test A | 2026-10-03 19:39:55 | 14 | 65073 |
| Piyush | api.teamcn.test A | 2026-10-03 19:40:03 | 11 | 3165 |

All queries: NOERROR, A 10.63.169.72, TTL 60, SERVER 10.63.169.3#53. Both dscacheutil -q host -a name app.teamcn.test outputs show name app.teamcn.test and ip_address 10.63.169.72.

Task B complete: private records configured, two other Macs configured to use Nitin DNS, explicit and default queries passed. HTTPS access through domain remains a later integration check.
