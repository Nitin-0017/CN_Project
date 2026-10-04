# Phase 1 Project Status

**Team:** Nitin Kumar, Kartik Yadav and Piyush Yadav  
**Documentation updated:** 4 October 2026  
**Scope:** Phase 1

The Phase 1 implementation and recorded functional tests are complete. Form submission, demonstration video and faculty evaluation are not marked complete without confirmation.

## 1. Requirement Status

| Requirement | Status | Supporting Documentation |
|---|---|---|
| A — LAN inventory and topology | Verified on the hotspot LAN | [Architecture](Architecture.md), [Ping Checks](03_Ping_Checks.md) |
| B — Private DNS and two configured clients | Verified on Kartik and Piyush | [DNS Setup](../configs/DNS_Setup.md) |
| C — Backend endpoints and identifiers | Both backends verified | [Backend Setup](../backend/README.md) |
| D — Reverse proxy and load balancing | HTTP and HTTPS responses from A and B verified | [nginx Setup](../configs/NGINX_Setup.md) |
| E — HTTPS and certificate trust | Certificate verification passed on all three Macs | [Client Trust](../configs/TLS_Client_Trust.md) |
| F — Conditional HTTP caching | HTTP 200 followed by matching HTTP 304 verified | [Caching Test](05_Caching_Test.md) |
| G — DNS, TCP and TLS packet evidence | Original capture analysed; screenshots retained | [Packet Capture](06_Packet_Capture.md) |
| Five failure scenarios and recovery | All five verified | [Failure Demonstrations](07_Failure_Demonstrations.md) |
| Source, configuration and evidence files | Prepared | [Evidence Index](../evidence/INDEX.md) |
| Submission form | Answers being prepared | Submission confirmation pending |
| Demonstration video | Required by the form | Completion not yet confirmed |
| Faculty checkpoint and individual viva | To be presented by the group | [Demo Guide](Demo_Guide.md), [Viva Notes](Viva_Notes.md) |

## 2. Recorded Working Configuration

The final recovery test was completed on 3 October 2026.

| Machine | IP Address | Services |
|---|---|---|
| Nitin | 10.63.169.3 | DNS port 53 and Backend A port 3001 |
| Kartik | 10.63.169.72 | nginx HTTP port 8080 and HTTPS port 8443 |
| Piyush | 10.63.169.63 | Backend B port 3002 and client tests |

Network details:

- Kartik's phone hotspot
- Subnet: 10.63.169.0/24
- Gateway: 10.63.169.210
- Active interface: en0 on all three Macs

Both DNS records point to the edge:

```text
app.teamcn.test → 10.63.169.72
api.teamcn.test → 10.63.169.72
```

These values describe the recorded setup. They do not imply that services remain running after terminals are closed.

## 3. Verified Results

- All six directional ping tests received four replies with zero loss.
- Both backends returned HTTP 200 with correct identifiers.
- Kartik and Piyush resolved both domains through the private DNS server.
- External DNS forwarding succeeded.
- nginx served requests from both backends.
- HTTPS certificate verification passed on all three Macs.
- The cache endpoint returned matching ETags across backends and a bodyless 304 response.
- The saved capture verified DNS resolution, TCP connection establishment and TLS negotiation.
- All five failure scenarios were followed by successful recovery.

The initial HTTP tests included timeouts. A later repeat succeeded, but the original delay's cause was not conclusively established.

## 4. Public DNS Comparison

On 4 October 2026, Nitin ran:

```bash
dig @8.8.8.8 app.teamcn.test A +time=3 +tries=1
```

The query returned NXDOMAIN from Google's public DNS server. This output was used for the form's public DNS comparison.

## 5. Evidence Coverage

The evidence folder contains terminal records, screenshots and the original packet capture.

- LAN inventory and initial ping proof are recorded as terminal text.
- DNS client verification includes screenshots.
- HTTPS verification is recorded through curl.
- Caching includes the HTTP 200 and conditional 304 evidence.
- DNS, TCP and TLS have focused Wireshark screenshots.
- Wrong-record failure and recovery are supported by terminal text.

Browser verification is not claimed. The HTTPS tests used curl with certificate validation enabled.

## 6. Remaining Submission and Presentation Work

1. Finish and review the submission form.
2. Include the requested failure demonstration in the video.
3. Check that repository image and document links open correctly.
4. Rehearse the live demonstration and individual viva.
5. Recheck IP addresses and restart services before any new live demonstration.

Screenshots added to a video should be identified as recorded evidence rather than a live terminal demonstration.

## 7. Related Documents

- [Architecture](Architecture.md)
- [Demo Guide](Demo_Guide.md)
- [Historical Timeline](History.md)
- [Evidence Index](../evidence/INDEX.md)

