# Backend Validation

Validation was completed using code checks and real terminal tests on 3 October 2026.

## 1. Code Checks

Syntax and in-memory response checks passed for:

- Backend A and B identifiers
- GET and HEAD handling
- Cache-Control headers
- Matching ETags across both backends
- Conditional 304 responses
- Unknown-path 404 responses

The assistant environment could not run a local HTTP socket test because of an environment restriction. Live operation was subsequently verified on the team's Macs.

## 2. Live Backend Startup

Recorded terminal outputs confirmed:

- Nitin: Backend A listening on `0.0.0.0:3001`
- Piyush: Backend B listening on `0.0.0.0:3002`

## 3. LAN Reachability

Kartik tested `/` and `/api/status` on both backends:

- Backend A: `http://10.63.169.3:3001`
- Backend B: `http://10.63.169.63:3002`

All four requests returned HTTP 200 with the correct X-Backend header and JSON response.

## 4. nginx and HTTPS Tests

Requests through `https://app.teamcn.test:8443/api/status` returned HTTP 200 responses from both backends.

Verbose curl tests confirmed successful TLS certificate verification. Six-request HTTPS tests showed both A and B in the responses.

## 5. Cache Validation

Piyush requested `/api/cache` through HTTPS and received:

- HTTP 200 from Backend B
- Cache-Control: public, max-age=60
- An ETag

A subsequent request using the matching If-None-Match header returned HTTP 304 from Backend A with the same ETag and no response body.

## 6. Failure and Recovery Tests

- Stopping Backend A resulted in six successful responses from Backend B.
- Restarting Backend A restored responses from both backends.
- With both backends stopped, nginx returned HTTP 502 while DNS and TLS still worked.
- After backend recovery, all six requests returned HTTP 200 and both backend identifiers appeared.

## 7. Evidence

See the [Evidence Index](../evidence/INDEX.md) for recorded terminal outputs, screenshots and packet capture verification.
