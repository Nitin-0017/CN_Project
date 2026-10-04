# Wrong Client DNS Failure

Owner: Piyush. User-supplied terminal output and original screenshot. Screenshot saved as Piyush_failure_wrong_DNS.jpg.

Changed Wi-Fi DNS to 8.8.8.8; getdnsservers confirmed 8.8.8.8. dig app.teamcn.test A +time=3 +tries=1 at 2026-10-03 20:47:10 IST returned NXDOMAIN, ANSWER 0, SERVER 8.8.8.8#53, query time 42 ms, ID 27058.

ping -c 4 10.63.169.72 returned 4/4 replies with 0.0% packet loss; RTT min/avg/max/stddev 10.011/51.730/87.545/28.438 ms.

Demonstrates wrong resolver lacks the team's private record while direct IP connectivity remains available. Nitin DNS service was not stopped. Restoration verified at 2026-10-03 20:48:14 IST: getdnsservers 10.63.169.3; dig NOERROR, one A answer 10.63.169.72, TTL60, SERVER 10.63.169.3#53, query13ms, ID18704. Original restore screenshot saved as Piyush_restore_DNS.jpg. Test and restoration complete.
