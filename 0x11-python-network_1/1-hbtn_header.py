#!/usr/bin/python3
"""
display the value of X-Request-Id
"""
import sys
import urllib.request

if __name__ == "__main__":
    url_passed = sys.argv[1]
    with urllib.request.urlopen(url_passed) as req:
        print(req.headers.get("X-Request-Id"))
