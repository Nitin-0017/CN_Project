# Phase 1 — nginx Log Findings

## 1. Evidence Source

This document summarizes the supplied nginx logs and OpenSSL terminal output.

The original text is preserved in [Original nginx Logs and OpenSSL Output](18_nginx_logs_openssl_original.txt).

These findings relate to the initial HTTP setup and timeout investigation.

## 2. Initial HTTP Request Observations

The supplied access log contains:

- Four GET requests recorded with status **499**, with upstream selection alternating between A and B.
- Subsequent successful requests recorded with status **200**, reaching both backends.

The error log reports that the client prematurely closed the connection while nginx was connecting to an upstream.

## 3. Interpretation of the 499 Entries

The log entries are consistent with curl abandoning the initial requests when its configured time limit expired.

They record the client closing the connection before nginx completed the response. They do not establish the underlying cause of the upstream connection delay.

The evidence does not prove that DNS, firewall settings or either backend caused the initial timeouts.

The corresponding client results are recorded in [Initial HTTP Load-Balancing Test](16_initial_http_load_balancing.md).

## 4. Separate 400 Request Observations

Other requests in the supplied logs returned **400** and began with escaped bytes corresponding to:

```text
16 03 01
```

These bytes are consistent with the beginning of a TLS handshake record sent to a plain HTTP listener.

This is a protocol-mismatch inference. The source application was not identified.

These entries are separate from the four GET requests recorded with status 499 and do not establish the cause of those timeouts.

## 5. HTTP and HTTPS Listener Usage

The initial HTTP listener used port **8080**. HTTPS was subsequently configured on port **8443**.

Use the matching URL scheme and listener port:

```text
http://app.teamcn.test:8080/api/status
```

```text
https://app.teamcn.test:8443/api/status
```

The final HTTPS setup and certificate validation are documented separately.

## 6. Recorded OpenSSL Details

The supplied command lookup identified:

```text
/opt/homebrew/bin/openssl
```

The supplied version output reported:

```text
OpenSSL 4.0.3 29 Sep 2026
```

The library version matched the reported OpenSSL version.

These values are recorded from the supplied terminal output.

## 7. Subsequent Verification

A repeat HTTP test returned six successful **HTTP 200** responses with backend identifiers:

```text
A → B → A → B → A → B
```

TLS configuration, certificate distribution and trusted HTTPS access were subsequently verified.

The successful later tests do not establish the cause of the earlier timeouts. No configuration change was reported between the initial mixed results and the successful HTTP repeat.

## 8. Related Evidence

- [Original nginx Logs and OpenSSL Output](18_nginx_logs_openssl_original.txt)
- [Initial HTTP Load-Balancing Test](16_initial_http_load_balancing.md)
- [Successful HTTP Round-Robin Test](17_http_round_robin_verified.md)
- [TLS Certificate Metadata](19_tls_certificate_metadata.md)
- [HTTPS Certificate Verification](20_https_cacert_verified.md)
- [HTTPS System Trust Verification](23_https_system_trust_verified.md)
