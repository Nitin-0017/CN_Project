# Wrong DNS Record Failure

User-supplied Piyush output. Flushed macOS cache via dscacheutil and HUP mDNSResponder before test.

At2026-10-03 21:16:30 IST dig app.teamcn.test A returned NOERROR but incorrect A10.63.169.3, TTL60, SERVER10.63.169.3#53, query61ms, ID64238.

Normal HTTPS curl resolved app.teamcn.test to10.63.169.3 and attempted TCP8443 from client10.63.169.63:50332; connection refused, curl7 after1079ms. Thus resolution succeeded but pointed to the wrong destination; failure occurred before TLS/HTTP.

Original screenshot not received. Correct-record restoration and successful HTTPS remain pending. Nitin fault DNS process last reported17542; verify current process identity before terminating for restore. Intended final configs in submission remain correct.

Nitin restoration output received: original backup copied back; cat shows app and api host-records both10.63.169.72. Syntax check OK. New foreground dnsmasq PID21865 started version2.93, upstream10.63.169.210#53, local teamcn.test zone, cleared cache and active forwarding logs. Client restored resolution/HTTPS still pending.

Recovery verified after Piyush flushed cache: dig at2026-10-03 21:21:22 IST NOERROR, A10.63.169.72 TTL60, server10.63.169.3#53,121ms, ID41945. Ordinary trusted HTTPS returned200 backendA at15:51:29 UTC=21:21:29 IST. Earlier wrong-IP curl in the same pasted message is historical pre-flush failure. Test and restoration complete. Recovery screenshot not received; supplied text evidence preserved.
