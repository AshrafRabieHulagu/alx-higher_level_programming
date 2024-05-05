#!/usr/bin/python3
"""Display X-Request-Id variable found in the header of the response.
"""
import urllib.request
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    req = urllib.request.Request(url)
    with urllib.request.urlopen(url) as response:
        html = response.info()
        print(html.get('X-Request-Id'))
