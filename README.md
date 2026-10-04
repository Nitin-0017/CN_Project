# Computer Networks Phase 1 Submission

Team: Nitin Kumar, Kartik Yadav, Piyush Yadav. Platform: three macOS laptops on Kartik phone hotspot. Build tasksA-G and all five controlled failure demonstrations verified from supplied outputs; live faculty checkpoint and individual viva remain to be presented.

## Start here

- docs/Architecture.md: topology, roles, IP/service inventory and flow.
- docs/Progress.md: final verified status and evidence limits.
- docs/Demo_Guide.md: named launch and live presentation sequence.
- docs/Viva_Notes.md: concepts for all members.
- docs/07_Failure_Demonstrations.md: all five actual outcomes/restorations.
- backend/server.py and README.md: sharedA/B source and launch instructions.
- configs/dnsmasq-phase1.conf: correct working DNS.
- configs/nginx-phase1-https.conf: current intended nginx config; deploy as edge/nginx.conf on Kartik.
- configs/tls-server.cnf, TLS_Setup.md, TLS_Client_Trust.md and server.crt: certificate generation/trust notes and verified public certificate.
- configs/DNS_Rollback.md: original clientDNS restore commands.
- evidence/: original screenshots, pcapng and documented results.

## Deployment facts

Nitin10.63.169.3: DNS53 and BackendA3001. Kartik10.63.169.72: nginxHTTPS8443 and HTTP8080. Piyush10.63.169.63: BackendB3002. Zone teamcn.test app/api both point to Kartik. Default DNS clients Kartik and Piyush use Nitin. Nitin HTTPS test used --resolve without changing his systemDNS.

## Evidence interpretation

Original images/files retained; terminal-only results are explicitly documented as transcriptions. Historic college-network inventory/pings and initial timeout investigation are preserved separately from current verified hotspot state. Demo fault configs and HTTP-only config are reference variants; deploy correct current DNS and HTTPS configs. No private key is included; server.key must stay on Kartik. Historical statuses in History.md are superseded by Progress.md.

Phase2 is not included. No faculty marks or viva performance claimed. IPs may change when reconnecting; recheck before demo. Source PDF: CN_Project_Doc.pdf supplied by user.
