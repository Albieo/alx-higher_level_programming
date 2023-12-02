#!/usr/bin/python3
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: ./7-error_code.py <URL>")
        sys.exit(1)

    url = sys.argv[1]

    try:
        r = requests.get(url)
        print(r.text)
        if r.status_code >= 400:
            print("Error code: {}".format(r.status_code))
    except requests.RequestException as e:
        print("Error accessing the URL: {}".format(e))
