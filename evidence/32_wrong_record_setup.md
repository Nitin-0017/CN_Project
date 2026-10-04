# Phase 1 — Wrong DNS Record Fault Setup

## 1. Evidence Source

This document summarizes Nitin's supplied terminal outputs from **2026-10-03**.

It records preparation of the wrong-record demonstration. The subsequent client failure and successful restoration are documented in [Wrong Record Failure and Recovery](33_wrong_record_failure.md).

The evidence is transcribed terminal output. Original screenshots for this setup are not linked here.

## 2. Before State — Correct DNS Records

The working project configuration maps both names to Kartik's nginx host:

| DNS Name | Correct IPv4 Address |
|---|---|
| app.teamcn.test | 10.63.169.72 |
| api.teamcn.test | 10.63.169.72 |

Working configuration:

```text
~/Documents/CN_Phase1/configs/dnsmasq-phase1.conf
```

## 3. Backup and DNS Process Stop

Before changing the record, Nitin created a backup at:

```text
~/Documents/CN_Phase1/configs/dnsmasq-phase1-backup.conf
```

The previous dnsmasq process, recorded as PID **63944**, logged that it exited after receiving **SIGTERM**.

This PID belongs to the historical test session and must not be reused as a current process ID.

## 4. Fault Introduced

Only the `app.teamcn.test` record was changed to Nitin's address instead of Kartik's nginx address.

| DNS Name | Fault Configuration |
|---|---|
| app.teamcn.test | 10.63.169.3 — incorrect nginx destination |
| api.teamcn.test | 10.63.169.72 — unchanged |

The changed app record was:

```ini
host-record=app.teamcn.test,10.63.169.3
```

The api record remained:

```ini
host-record=api.teamcn.test,10.63.169.72
```

The fault therefore changed the DNS answer rather than the client's selected DNS server.

## 5. Validation and Restart

The modified configuration passed the dnsmasq syntax check.

The initial supplied restart output ended at the administrator password prompt. Later supplied query logs showed a new dnsmasq process, PID **17542**, actively responding to and forwarding client queries.

Those later logs establish that the restart completed. PID **17542** is also a historical process identifier.

## 6. Subsequent Client Failure Test

Piyush subsequently tested the faulty record.

The recorded results showed:

- DNS returned **NOERROR** with the incorrect address **10.63.169.3**.
- curl attempted the HTTPS connection to that address on port **8443**.
- The connection was refused.

Detailed results are recorded in [Wrong Record Failure and Recovery](33_wrong_record_failure.md).

## 7. Restoration Status

The correct DNS backup was subsequently restored and syntax validation passed.

After DNS restart and client cache clearing, the recorded client test returned:

- The correct A answer **10.63.169.72**.
- A successful HTTPS **HTTP 200** response from Backend A.

The fault and recovery are complete in the recorded evidence.

## 8. Configuration Scope

The repository's [dnsmasq-phase1.conf](../configs/dnsmasq-phase1.conf) contains the correct working records.

The wrong-record variant is retained separately for demonstration reference. The working project configuration must resolve both app and api names to **10.63.169.72**.

## 9. Related Evidence

- [Working DNS Configuration](../configs/dnsmasq-phase1.conf)
- [DNS Setup Instructions](../configs/DNS_Setup.md)
- [Default Client DNS Verification](13_default_dns_verified.md)
- [Wrong Record Failure and Recovery](33_wrong_record_failure.md)
- [Failure Demonstration Results](../docs/07_Failure_Demonstrations.md)
