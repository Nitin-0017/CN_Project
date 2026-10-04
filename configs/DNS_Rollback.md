# Restore Original Wi Fi DNS

Original settings were captured before project DNS modification on 2026-10-03. Run these only when restoring settings after the demo or leaving the project network, not during the running project.

## Kartik Yadav

Restore automatic DNS:

```sh
sudo networksetup -setdnsservers "Wi-Fi" Empty
```

## Piyush Yadav

Restore original manual entries in their recorded order:

```sh
sudo networksetup -setdnsservers "Wi-Fi" 8.8.8.8 4.2.2.2
```

## Both clients

Verify restored settings:

```sh
networksetup -getdnsservers "Wi-Fi"
```

Project setting during demo is 10.63.169.3 only. Nitin's DNS must stay running on the same hotspot. If Nitin's IP changes, update configurations and clients. Switching networks with this project resolver still configured may break DNS; restore original settings when done.
