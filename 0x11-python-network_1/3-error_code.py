#!/usr/bin/python3
""" ERROR CODES TO BE HANDLED"""
import urllib.request
from urllib.error import HTTPError
import sys


if __name__ == "__main__":
    try:
        with urllib.request.urlopen(sys.argv[1]) as response:
            dedata = response.read()
            dedata = dedata.decode("UTF-8")
            print(dedata)
    except HTTPError as e:
        print('Error code: {}'.format(e.code))
