#!/usr/bin/python3
import requests


if __name__ == "__main__":
    r = requests.get('https://alx-intranet.hbtn.io/status')

    raw_body = r.text

    lines = ["Body response:",
             f"\t- type: {type(raw_body)}",
             f"\t- content: {raw_body}"]

    for line in lines:
        print(line)
