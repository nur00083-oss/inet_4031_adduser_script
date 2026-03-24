#!/usr/bin/env python3

import sys
import os

# Loop through each line from input file
for line in sys.stdin:
    line = line.strip()

    # Skip empty lines or comments
    if not line or line.startswith("#"):
        continue

    # Split input line by colon
    parts = line.split(":")

    # Make sure the line has exactly 5 fields
    if len(parts) != 5:
        continue

    # Assign values from input line
    username = parts[0]
    password = parts[1]
    lastname = parts[2]
    firstname = parts[3]
    groups = parts[4]

    # Create user
    print(f"Creating user: {username}")
    os.system(f"sudo useradd -m -c '{firstname} {lastname}' {username}")

    # Set password
    os.system(f"echo '{username}:{password}' | sudo chpasswd")

    # Add to groups if not "-"
    if groups != "-":
        group_list = groups.split(",")
        for group in group_list:
            os.system(f"sudo usermod -aG {group} {username}")
