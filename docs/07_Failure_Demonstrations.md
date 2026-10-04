# Phase 1 Failure Demonstration Results

| Fault | Member actions | Actual observation | Restoration |
|---|---|---|---|
| Wrong client DNS | Piyush sets8.8.8.8 | NXDOMAIN; direct IP ping4/4 | DNS10.63.169.3, correct answer verified |
| Wrong record IP | Nitin changes app record to10.63.169.3; Piyush tests | NOERROR wrongIP; curl refused8443 | Backup restored; correct lookup and200A |
| A stopped | Nitin stopsA; Piyush tests | Six200B | Recovery B/B/A/B/A/B all200 |
| A and B stopped | Nitin/Piyush stop backends; Kartik tests | DNS/TLS work;502 | Six200 B/B/A/B/A/B |
| Wrong destination port | Piyush targets8444 | DNS works; connection refused | Correct8443 returns200B |

All five tests and restored service state verified from supplied outputs. Detailed evidence is in files28-33. Perform one fault at a time during demo and restore before the next. Do not use fault DNS template as the working configuration.
