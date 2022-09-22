#!/usr/bin/python3
import sys
if len(sys.argv) == 0:
    print("{} arguments.".format(0))
else:
    for i in range(len(sys.argv)):
        print("{}: {}".format(i + 1, sys.argv[i]))
