#!/usr/bin/python3
"""
send POST request
"""
import sys
import urllib.request
import urllib.parse

if __name__ = "__main__":
    url = sys.argv[1]
    email = {'email': sys.argv[2]}
    data = urllib.parse.urlencode(email).encode("ascii")

    request = urllib.request.Request(url, data)
    with urllib.request.urlopen(url) as req:
        print(req.read().decode('utf-8'))
