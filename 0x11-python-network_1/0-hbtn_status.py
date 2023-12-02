#!/usr/bin/python3
"""This module fetches data from a URL
and prints information about the response."""
import urllib.request


if __name__ == "__main__":
    url = 'https://alx-intranet.hbtn.io/status'

    with urllib.request.urlopen(url) as response:
        raw_body = response.read()
        body = raw_body.decode('utf-8')

    lines = ["Body response:",
             f"\t- type: {type(raw_body)}",
             f"\t- content: {raw_body}",
             f"\t- utf8 content: {body}"]

    for line in lines:
        print(line)
