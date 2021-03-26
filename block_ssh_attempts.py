#!/usr/bin/python3

# importing required package
import linecache

# extracting the log file
invalidusers = linecache.getline('sshdlog.asc', "Invalid")

# print the line from log file
print(invalidusers)
