# Wrong Destination Port Failure

User supplied Piyush terminal output and original screenshot saved as Piyush_failure_wrong_port.jpg.

DNS at 2026-10-03 20:51:08 IST: NOERROR, A 10.63.169.72, TTL60, SERVER10.63.169.3#53, 29ms, queryID57431.

HTTPS request to app.teamcn.test:8444 resolved correctly but connection from client10.63.169.63:50164 to edge10.63.169.72:8444 was refused. curl error7 after1070ms. Thus TCP service port failed despite valid DNS resolution.

Correct-port request to :8443 returned HTTP/1.1 200 OK, nginx1.31.6, X-BackendB, statusok JSON, at 2026-10-03 15:21:25 UTC =20:51:25 IST. No trust bypass used. No configuration change needed for restoration; correct endpoint verified. Test complete.
