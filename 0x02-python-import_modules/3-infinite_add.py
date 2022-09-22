#!/usr/bin/python3
import sys
count = 0
for i in range(len(sys.argv)):
    count += int(sys.argv[i])
print(count)
