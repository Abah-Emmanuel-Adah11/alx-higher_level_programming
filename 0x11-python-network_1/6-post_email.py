#!/usr/bin/python3
# A python script that sends email
import requests
import sys

try:
    data = {'email': sys.argv[2]}
    res = requests.post(sys.argv[1], data)
    print(res.text)
except BaseException:
    pass
