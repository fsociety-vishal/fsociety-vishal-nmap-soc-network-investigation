import subprocess
import re

# Get recent kernel/UFW logs
result = subprocess.run(
    ["journalctl", "-k", "--since", "10 minutes ago"],
    capture_output=True,
    text=True
)

logs = result.stdout

print("=== Security Events ===")

for line in logs.splitlines():
    if "UFW" not in line:
        continue

    src = re.search(r"SRC=([0-9.]+)", line)
    dst = re.search(r"DST=([0-9.]+)", line)
    dpt = re.search(r"DPT=(\d+)", line)
    proto = re.search(r"PROTO=(\w+)", line)

    if dpt and dpt.group(1) in ["21", "22", "23", "80", "443"]:
        print("Source IP:", src.group(1) if src else "N/A")
        print("Destination IP:", dst.group(1) if dst else "N/A")
        print("Destination Port:", dpt.group(1))
        print("Protocol:", proto.group(1) if proto else "N/A")
        print("-" * 40)
