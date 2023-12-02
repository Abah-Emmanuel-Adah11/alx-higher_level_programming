#!/usr/bin/python3
""" A python script that use requests for making requests
"""

if __name__ == "__main__":
    import requests as req
    r = req.get('https://intranet.hbtn.io/status')
    print("Body response:")
    print("\t- type:", type(r.text))
    print("\t- content:", r.text)
