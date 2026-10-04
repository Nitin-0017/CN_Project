# Client Certificate Trust Commands

Source: member-labelled terminal outputs supplied by the user on 2026-10-03. All three ran sudo security add-trusted-cert -d -r trustRoot -p ssl -k /Library/Keychains/System.keychain with their verified public server.crt path. Each command returned to prompt without displayed error.

Kartik used ~/Documents/CN_Phase1/edge/certs/server.crt. Nitin and Piyush used ~/Documents/CN_Phase1/certs/server.crt. Passwords not supplied or stored.

This records completed commands without reported errors; working client trust remains pending ordinary HTTPS curl tests without --cacert or -k. Nitin's default DNS remains unchanged; his planned --resolve test does not prove a DNS lookup.
