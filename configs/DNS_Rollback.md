# Restore Original Wi-Fi DNS Settings

The original DNS settings were recorded on 3 October 2026 before configuring the project DNS.

Use these rollback commands after the demonstration or when leaving the project network.

## 1. Kartik — Restore Automatic DNS

Kartik originally had no manually configured Wi-Fi DNS servers.

Run on Kartik's Mac:

```bash
sudo networksetup -setdnsservers "Wi-Fi" Empty
```

## 2. Piyush — Restore Original DNS Servers

Piyush's original Wi-Fi DNS servers were:

```text
8.8.8.8
4.2.2.2
```

Run on Piyush's Mac:

```bash
sudo networksetup -setdnsservers "Wi-Fi" 8.8.8.8 4.2.2.2
```

## 3. Verify Restored Settings

Run on each client:

```bash
networksetup -getdnsservers "Wi-Fi"
```

Expected results:

- **Kartik:** No manually configured DNS servers.
- **Piyush:** `8.8.8.8` followed by `4.2.2.2`.

## 4. Original Settings Evidence

The recorded terminal output is available in:

[Original DNS Settings and Forwarding Evidence](../evidence/12_original_dns_and_forwarding.md)

This evidence records the original settings before the project DNS changes. The screenshots below show the later project configuration.

## 5. Project DNS Configuration

During the demonstration, Kartik and Piyush used Nitin's private DNS server:

```text
10.63.169.3
```

To configure the project DNS on either client:

```bash
sudo networksetup -setdnsservers "Wi-Fi" 10.63.169.3
networksetup -getdnsservers "Wi-Fi"
```

Nitin's dnsmasq must be running and reachable on the project network.

### Kartik — Project DNS Screenshot

The screenshot shows DNS server `10.63.169.3` and successful resolution of the project domains to nginx edge IP `10.63.169.72`.

![Kartik project DNS configuration and resolution](../evidence/Kartik_default_DNS.png)

### Piyush — Project DNS Screenshot

The screenshot shows DNS server `10.63.169.3` and successful resolution of the project domains to nginx edge IP `10.63.169.72`.

![Piyush project DNS configuration and resolution](../evidence/Piyush_default_DNS.jpg)

## 6. DNS Failure Test Recovery

After the wrong-DNS failure demonstration, Piyush restored the project DNS server to `10.63.169.3`.

The subsequent query returned `NOERROR` and the correct edge IP `10.63.169.72`.

![Piyush restores project DNS after the failure test](../evidence/Piyush_restore_DNS.jpg)

Restoring the project DNS after a failure test is different from restoring the original settings after completing the demonstration.

## 7. Network Changes

The recorded project DNS IP was `10.63.169.3`. If Nitin's IP changes after reconnecting, update the DNS configuration and client settings.

After finishing the demonstration, restore each client's original DNS settings before leaving the project network.
