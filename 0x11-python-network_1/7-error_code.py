#!/usr/bin/python3
# A python script that takes and send a URL to display a body of response.
import requests
import sys

try:
    res = requests.get(sys.argv[1])
    if res.status_code == requests.codes.ok:
        print(res.text)
    else:
        if res.status_code >= 400:
            print("Error code:", res.status_code)
except BaseException:
    pass
