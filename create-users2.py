#!/usr/bin/env python3

import sys
import os

print("Run in dry-run mode? (Y/N): ", end="", flush=True)
with open("/dev/tty", "r") as keyboard:
    dry_run = keyboard.readline().strip().lower()

for line in sys.stdin:
    line = line.strip()

    if not line:
        continue

    if line.startswith("#"):
        if dry_run == "y":
            print(f"Skipping line: {line}")
        continue

    parts = line.split(":")

    if len(parts) != 5:
        if dry_run == "y":
            print(f"Invalid line skipped: {line}")
        continue

    username = parts[0]
    password = parts[1]
    lastname = parts[2]
    firstname = parts[3]
    groups = parts[4]

    user_cmd = f"sudo useradd -m -c '{firstname} {lastname}' {username}"
    pass_cmd = f"echo '{username}:{password}' | sudo chpasswd"

    if dry_run == "y":
        print(f"DRY RUN: {user_cmd}")
        print(f"DRY RUN: {pass_cmd}")
    else:
        os.system(user_cmd)
        os.system(pass_cmd)

    if groups != "-":
        for group in groups.split(","):
            group_cmd = f"sudo usermod -aG {group} {username}"
            if dry_run == "y":
                print(f"DRY RUN: {group_cmd}")
            else:
                os.system(group_cmd)
