#!/usr/bin/python3
import urllib.request


url = 'https://alx-intranet.hbtn.io/status'

with urllib.request.urlopen(url) as response:
    raw_body = response.read()
    body = raw_body.decode('utf-8')

print("Body response:")
print("\t- type:", type(raw_body))
print("\t- content:", raw_body)
print("\t- utf8 content:", body)
