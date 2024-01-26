#!/usr/bin/python3
"""Displays the value of X-Request-Id and 

sends a request to the specified URL.
"""
import sys
import urllib.request


if __name__ == "__main__":
    url = sys.argv[1]

    request = urllib.request.Request(url)
    with urllib.request.urlopen(request) as response:
        print(dict(response.headers).get("X-Request-Id")
