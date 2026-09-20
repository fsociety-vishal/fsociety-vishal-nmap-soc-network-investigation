# Project Documentation

## 1. Project Overview

This project was performed as a small SOC-style security investigation using Kali Linux and Ubuntu virtual machines. The objective was to generate network activity with Nmap, investigate the resulting activity through Ubuntu logs, analyze relevant UFW events with Python, and validate the firewall configuration.

## 2. Lab Workflow

1. Kali Linux — reconnaissance
2. Ubuntu — target and log source
3. SSH — remote access and investigation
4. UFW — firewall configuration and logging
5. Python — basic UFW log filtering
6. SCP — evidence transfer
7. Nmap / service checks — validation

## 3. Nmap Reconnaissance

A TCP SYN scan was performed against the Ubuntu target:

```bash
sudo nmap -sS -p 21,22,23,80,443 <TARGET_IP>
```

The scan showed SSH on port 22 as open while the other selected ports were filtered.

Service detection was then used:

```bash
sudo nmap -sV -p 21,22,23,80,443 <TARGET_IP>
```

This identified the SSH service running on the Ubuntu system.

## 4. Log Investigation

Ubuntu logs were reviewed with:

```bash
sudo journalctl --since "10 minutes ago"
```

UFW-related kernel events were then filtered:

```bash
sudo journalctl -k --since "5 minutes ago" | grep -i ufw
```

The logs contained useful network information such as source address, destination address, port, protocol, and timestamp.

## 5. SSH Verification

SSH was enabled, started, and checked:

```bash
sudo systemctl enable ssh
sudo systemctl start ssh
sudo systemctl status ssh
```

The service was active and listening on port 22.

## 6. UFW Configuration

The firewall was configured with:

```bash
sudo ufw allow ssh
sudo ufw enable
sudo ufw logging medium
sudo ufw status verbose
```

This enabled UFW, allowed SSH access, and enabled medium-level logging.

## 7. Python Log Analysis

The Python script in `scripts/log_analyzer.py` reads recent kernel logs using `journalctl`, keeps UFW entries, extracts source IP, destination IP, destination port, and protocol, and prints events for ports 21, 22, 23, 80, and 443.

In simple terms:

> Python takes the raw UFW logs and makes selected network details easier to read.

## 8. Evidence Collection

Screenshots were transferred from Ubuntu to the Windows analyst workstation using SCP.

The screenshots in this repository have been redacted to hide the exact IP addresses. The first two octets are retained where possible so the network context remains understandable.

## 9. Validation

The firewall and SSH listener were checked after the configuration:

```bash
sudo ufw status numbered
sudo ss -lntp | grep ':22'
```

These checks confirmed the firewall rule and SSH listener state.

## 10. Conclusion

The lab provided hands-on practice with network reconnaissance, Linux service verification, UFW configuration, security log investigation, basic Python log analysis, and evidence handling.
