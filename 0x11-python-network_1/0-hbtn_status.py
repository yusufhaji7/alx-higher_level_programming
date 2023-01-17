#!/usr/bin/python3
"""
script to fetch https://alx-intranet.hbtn.io/status
"""
import urllib.request

if __name__ == "__main__":
    with urllib.request.urlopen("https://alx-intranet.hbtn.io/status") as resp:
        read_resp = resp.read()
        print("Body response:")
        print("\t - type: {}".format(type(read_resp)))
        print("\t - content: {}".format(read_resp))
        print("\t - utf8 content: {}".format(read_resp.decode('utf-8')))
