#!/usr/bin/python3
"""Headers again, different module"""
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) < 2:
        q = ""
    else:
        q = sys.argv[1]
    dic = {'q': q}
    url = 'http://0.0.0.0:5000/search_user'
    r = requests.post(url, dic)
    try:
        rj = r.json()
        if rj == {}:
            print('No result')
        else:
            print('[{}] {}'.format(rj['id'], rj['name']))
    except:
        print('Not a valid JSON')
