# Nginx Validation and Launch

Source: Kartik terminal output supplied by user, received 2026-10-03. Exact execution timestamps not supplied.

```text
nginx -t -p "$HOME/Documents/CN_Phase1/edge/" -c nginx.conf
nginx: the configuration file /Users/kartikyadav/Documents/CN_Phase1/edge/nginx.conf syntax is ok
nginx: configuration file /Users/kartikyadav/Documents/CN_Phase1/edge/nginx.conf test is successful
```

Then ran:

```sh
nginx -p "$HOME/Documents/CN_Phase1/edge/" -c nginx.conf -g 'daemon off;'
```

No error or returned shell prompt is shown after launch. Foreground launch attempted; successful listener, proxy responses and A/B distribution require client HTTP tests and remain pending. Project config currently uses HTTP :8080 only; HTTPS is not configured yet.
