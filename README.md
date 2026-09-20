# Nmap SOC Network Investigation

Hands-on SOC lab covering Nmap reconnaissance, Ubuntu log analysis, UFW firewall configuration, Python-based log filtering, SSH investigation, evidence collection with SCP, and security validation.

## Objective

The project simulates a simple offensive-to-defensive workflow:

1. Kali Linux performs network reconnaissance against an Ubuntu target.
2. Ubuntu is checked for running services and SSH access.
3. System and UFW logs are reviewed for relevant network activity.
4. Python is used to filter and organize UFW log entries.
5. UFW is enabled and configured with SSH access and logging.
6. Evidence is collected from Ubuntu to Windows using SCP.
7. Firewall and service state are verified after the changes.

## Lab Setup

- **Kali Linux:** reconnaissance / attacker simulation
- **Ubuntu 20.04:** target / log source
- **Windows PowerShell:** remote analyst workstation
- **Nmap:** network reconnaissance and service detection
- **OpenSSH:** remote administration and investigation access
- **UFW:** host-based firewall
- **Python 3:** basic log analysis
- **SCP:** evidence transfer

## Key Commands

```bash
sudo nmap -sS -p 21,22,23,80,443 172.18.200.28
sudo nmap -sV -p 21,22,23,80,443 172.18.200.28

sudo journalctl --since "10 minutes ago"
sudo journalctl -k --since "5 minutes ago" | grep -i ufw

sudo systemctl enable ssh
sudo systemctl start ssh
sudo systemctl status ssh

sudo ufw allow ssh
sudo ufw enable
sudo ufw logging medium
sudo ufw status verbose

sudo ss -lntp | grep ':22'
ip addr show
```

## Main Findings

- The Ubuntu target was reachable from Kali.
- TCP port 22 was identified as an open SSH service.
- Nmap service detection identified OpenSSH on the Ubuntu system.
- UFW was initially inactive and was later enabled.
- SSH access was explicitly allowed through UFW.
- UFW logging was enabled at the medium level.
- Relevant firewall events were extracted from the kernel journal.
- Python output was used to make selected UFW events easier to review.
- Evidence was transferred to the Windows workstation using SCP.

## Evidence

All screenshots are stored in the `evidence/` directory and are named according to the stage of the investigation.

See [`docs/PROJECT_DOCUMENTATION.md`](docs/PROJECT_DOCUMENTATION.md) for the full project documentation.

## Note

This repository documents a controlled lab environment using virtual machines and private IP addresses. The activities were performed for authorized security testing and learning purposes.


## Python Log Analyzer

The Python script is intentionally simple. It does four main things:

1. Reads recent kernel logs using `journalctl`.
2. Keeps only lines containing `UFW`.
3. Extracts the source IP, destination IP, destination port, and protocol.
4. Displays events for ports 21, 22, 23, 80, and 443.

In simple terms: **Python takes the raw UFW logs and makes the important network details easier to read.**


## Evidence Privacy

The screenshots in this repository have been redacted to hide the exact IPv4 addresses while keeping enough network information to understand the investigation. The commands shown in the screenshots are also redacted where an IP address appears.
