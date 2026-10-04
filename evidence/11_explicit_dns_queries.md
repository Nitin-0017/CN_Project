# Explicit Client DNS Query Evidence

User-supplied dig outputs. All four use DiG 9.10.6 and server 10.63.169.3#53, return NOERROR, flags qr aa rd ra, one A answer, TTL 60 and 60 received bytes.

| Client | Name | A answer | Query time ms | Execution time IST | Query ID |
|---|---|---|---|---|---|
| Piyush | app.teamcn.test | 10.63.169.72 | 884 | 2026-10-03 19:33:47 | 18142 |
| Piyush | api.teamcn.test | 10.63.169.72 | 29 | 2026-10-03 19:33:59 | 2097 |
| Kartik | app.teamcn.test | 10.63.169.72 | 3482 | 2026-10-03 19:33:47 | 21403 |
| Kartik | api.teamcn.test | 10.63.169.72 | 96 | 2026-10-03 19:34:06 | 51963 |

Commands: dig @10.63.169.3 app.teamcn.test A and dig @10.63.169.3 api.teamcn.test A.

These tests explicitly choose Nitin's resolver. They do not prove either client's default/system resolver is configured to use it. External-name forwarding and existing DNS settings are not yet recorded. Original screenshots not supplied.
