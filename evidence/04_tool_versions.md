# Tool Version Evidence

## 1. Evidence Source

The versions below were recorded from member-labelled terminal outputs supplied on **2026-10-03**.

These are transcribed version results; original command execution timestamps were not supplied.

## 2. Commands Used

Each member ran:

```bash
brew --version
python3 --version
```

## 3. Recorded Versions

| Member | Homebrew Version | Python Version |
|---|---|---|
| Nitin Kumar | 6.0.20 | 3.13.1 |
| Kartik Yadav | 6.0.17 | 3.12.5 |
| Piyush Yadav | 7.0.6 | 3.14.2 |

## 4. Interpretation

All three members supplied successful Homebrew and Python version outputs.

The project backend uses the Python standard library and does not require third-party Python packages. The recorded Python versions meet the documented Python 3.12-or-later requirement.

Version outputs identify the installed tools at the time of recording. Service startup and network functionality are documented in separate evidence files.

## 5. Related Evidence

- [Backend Startup](07_backend_startup.md)
- [Backend HTTP Tests](08_backend_http_tests.md)
- [DNS Prerequisites](09_dns_prerequisites.md)
- [DNS Validation and Startup](10_dns_startup.md)
- [Original nginx Installation Output](14_nginx_install_original.txt)
- [nginx Validation and Launch](15_nginx_validation_launch.md)
- [Final Project Status](../docs/Progress.md)
