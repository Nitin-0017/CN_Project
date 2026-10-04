# Phase 1 — nginx Validation and Launch Evidence

## 1. Evidence Source

This document records Kartik's terminal output supplied on **2026-10-03**. Exact command execution timestamps were not supplied.

The commands and validation output below belong to the initial HTTP setup stage. Subsequent HTTP and HTTPS tests are linked separately.

This document contains transcribed terminal evidence.

## 2. Project Configuration Location

| Item | Value |
|---|---|
| nginx host | Kartik's Mac |
| Project IPv4 address | 10.63.169.72 |
| Project prefix | ~/Documents/CN_Phase1/edge/ |
| Active configuration filename | nginx.conf |
| Initial HTTP port | 8080 |
| Subsequent HTTPS port | 8443 |

The project uses a standalone nginx prefix and configuration.

## 3. Configuration Validation

### Command

```bash
nginx -t \
  -p "$HOME/Documents/CN_Phase1/edge/" \
  -c nginx.conf
```

### Recorded Output

```text
nginx: the configuration file /Users/kartikyadav/Documents/CN_Phase1/edge/nginx.conf syntax is ok
nginx: configuration file /Users/kartikyadav/Documents/CN_Phase1/edge/nginx.conf test is successful
```

The configuration passed nginx's validation check.

## 4. Foreground Launch

After successful validation, Kartik ran:

```bash
nginx \
  -p "$HOME/Documents/CN_Phase1/edge/" \
  -c nginx.conf \
  -g 'daemon off;'
```

### Recorded Observation

The supplied terminal output showed no launch error or returned shell prompt after this command.

This observation is consistent with a foreground process remaining active. Client requests provide the separate evidence that nginx served traffic successfully.

## 5. Initial Test Scope

At this stage, the project configuration used HTTP on port **8080**.

The validation output confirms that nginx accepted the configuration. It does not, by itself, prove successful backend connections, response forwarding or load distribution.

## 6. Subsequent Verification

Later tests recorded:

- Successful HTTP requests through the project domain.
- Six consecutive HTTP 200 responses with backend identifiers **A/B/A/B/A/B**.
- HTTPS configuration on port **8443**.
- Successful certificate validation and HTTPS responses.
- Backend failure and recovery behaviour.

The initial timeout observations are preserved separately; their cause was not established.

## 7. Configuration References

- [Initial HTTP Configuration](../configs/nginx-phase1-http.conf)
- [Final HTTPS Configuration](../configs/nginx-phase1-https.conf)
- [nginx Setup Instructions](../configs/NGINX_Setup.md)
- [TLS Setup Instructions](../configs/TLS_Setup.md)

For the final demonstration, the HTTPS configuration is deployed as `edge/nginx.conf` on Kartik's Mac.

## 8. Related Evidence

- [Original nginx Installation Output](14_nginx_install_original.txt)
- [Initial HTTP Load-Balancing Tests](16_initial_http_load_balancing.md)
- [Successful HTTP Round-Robin Tests](17_http_round_robin_verified.md)
- [Recorded Log Findings](18_log_findings.md)
- [HTTPS Certificate Verification](20_https_cacert_verified.md)
- [HTTPS System Trust Verification](23_https_system_trust_verified.md)
- [Single Backend Failure and Recovery](30_single_backend_failover.md)
- [Both Backends Down and Recovery](31_both_backends_down.md)
