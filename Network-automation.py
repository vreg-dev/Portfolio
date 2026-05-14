# Network Automation Tool
# Author: Gervasious Maingi (vreg-dev)
# Description: Automates repetitive network commands

import subprocess
import datetime

# List of commands to run
commands = [
    "ping -c 4 8.8.8.8",
    "ip addr show",
    "netstat -tuln",
    "nmap -sV localhost",
]

def run_command(cmd):
    print(f"\n[*] Running: {cmd}")
    print("-" * 40)
    result = subprocess.run(
        cmd, shell=True,
        capture_output=True,
        text=True
    )
    print(result.stdout)
    if result.stderr:
        print(f"[!] Error: {result.stderr}")

def main():
    print("=" * 40)
    print(" MKMK Network Automation Tool")
    print(f" {datetime.datetime.now()}")
    print("=" * 40)
    
    for cmd in commands:
        run_command(cmd)
    
    print("\n[✓] All commands completed.")

if __name__ == "__main__":
    main()
