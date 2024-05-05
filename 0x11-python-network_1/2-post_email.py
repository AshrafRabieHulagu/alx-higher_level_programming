#!/usr/bin/python3
import urllib.parse
import urllib.request
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    data = urllib.parse.urlencode({'email': email})
    data = data.encode('utf-8')
    with urllib.request.urlopen(url, data=data) as response:
        body = response.read()
        print(body.decode('utf-8'))
