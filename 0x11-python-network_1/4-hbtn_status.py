#!/usr/bin/python3
"""A simple script to fetch and display information
from a URL using the requests module.

This script sends a GET request to 'https://alx-intranet.hbtn.io/status'
using the requests module and displays information about the response body."""
import requests


if __name__ == "__main__":
    r = requests.get('https://alx-intranet.hbtn.io/status')

    raw_body = r.text

    lines = ["Body response:",
             f"\t- type: {type(raw_body)}",
             f"\t- content: {raw_body}"]

    for line in lines:
        print(line)
