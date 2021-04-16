#!/usr/bin/python3
ips = []


# Opens the "sshdlog" file and reads out each line
with open('sshdlog.asc') as file:
    for line in file.readlines():
        # Checks if "Invalid user" is in line and searches for the ip from the line
        if "Invalid user" in line:
            listLines=line.split(" ")
            ip=listLines[-3]
            ips.append(ip)
            print("Volgende ip is toegevoegd aan de lijst: " + ip)
# Next step is filtering the output and using fwblock.py to block the ip