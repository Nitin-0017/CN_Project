# Single Backend Failure Test

Nitin supplied screenshot showing Backend A foreground process interrupted with Ctrl C and shell prompt returned. DNS was not reported stopped.

Piyush supplied six sequential HTTPS curl responses to app.teamcn.test:8443/api/status. All six HTTP/1.1 200 OK, nginx1.31.6, X-Backend B, JSON backendB/statusok, Date2026-10-03 15:24:07 UTC=20:54:07 IST. No -k or --cacert used. Original images saved as Nitin_backend_A_stopped.png and Piyush_single_backend_failover.jpg. Full text confirms all six; screenshot bottom crops final response details.

Service continued using remaining Backend B when A stopped. Recovery verified by six subsequent HTTPS HTTP200 responses B/B/A/B/A/B at2026-10-03 15:26:57-58 UTC=20:56:57-58 IST. A responses establish A available again; separate restart console output was not supplied. Screenshot saved as Piyush_backend_A_recovery.jpg. First two B responses are consistent with passive failure timeout/re-entry, but exact timing cause not proven. Single-backend failure and recovery complete.
