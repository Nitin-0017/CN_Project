# Wrong Record Fault Setup

Nitin supplied terminal output. Old dnsmasq PID63944 logged exiting on receipt of SIGTERM. Backup created at ~/Documents/CN_Phase1/configs/dnsmasq-phase1-backup.conf before exact replacement.

Fault config app.teamcn.test ->10.63.169.3 (Nitin) instead of real edge10.63.169.72. api.teamcn.test remains10.63.169.72. Config syntax check OK.

Foreground restart command invoked; latest supplied output ends at Password:. Subsequent user output shows new dnsmasq PID17542 actively responding and forwarding client queries; restarted process activity verified. Wrong app record answer still requires client test. Piyush wrong-record query/connection test not performed yet. Restore original backup before declaring full Phase1 complete. Bundle configs/dnsmasq-phase1.conf retains correct intended final configuration; fault variant saved separately.
