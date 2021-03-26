#!/usr/bin/python3

# Opens the "sshdlog" file
with open('sshdlog.asc') as file:
    # Reads all the lines
    for line in file.readlines():
        # Checks if "Invalid" is in any of the lines
        if "Invalid" in line:
            # Prints those lines
            print(line)
