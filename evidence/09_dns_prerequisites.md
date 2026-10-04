# DNS Prerequisite Evidence

User outputs received 2026-10-03 confirm dnsmasq 2.93 installation at /opt/homebrew/Cellar/dnsmasq/2.93, brew --prefix = /opt/homebrew, and no displayed listeners for sudo lsof -nP -iUDP:53 -iTCP:53. Blank lsof output suggests no listed TCP/UDP listener on 53 at the check time; DNS launch is still pending.

Homebrew's unrelated MongoDB tap-trust notice did not prevent dnsmasq installation. No tap trust changes are needed for this project step.
