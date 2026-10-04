# Current Hotspot Peer Connectivity Checks

Run each command separately on its assigned Mac. Share full output and capture the command, replies and packet-loss summary. All results below passed according to user-supplied outputs. Earlier college-network pings do not establish hotspot connectivity.

## Nitin Kumar

```sh
ping -c 4 10.63.169.72
ping -c 4 10.63.169.63
```

## Kartik Yadav

```sh
ping -c 4 10.63.169.3
ping -c 4 10.63.169.63
```

## Piyush Yadav

```sh
ping -c 4 10.63.169.3
ping -c 4 10.63.169.72
```

## Results

| Source | Destination | Result |
|---|---|---|
| Nitin | Kartik | Passed: 4/4 replies, 0.0% loss |
| Nitin | Piyush | Passed: 4/4 replies, 0.0% loss |
| Kartik | Nitin | Passed: 4/4 replies, 0.0% loss |
| Kartik | Piyush | Passed: 4/4 replies, 0.0% loss |
| Piyush | Nitin | Passed: 4/4 replies, 0.0% loss |
| Piyush | Kartik | Passed: 4/4 replies, 0.0% loss |

Screenshots: NAME_hotspot_ping_TARGET.png, one per direction. If timeouts occur, share them before changing firewall or network settings.
