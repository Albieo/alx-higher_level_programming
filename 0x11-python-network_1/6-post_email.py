#!/usr/bin/python3
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: ./6-post_email.py <URL> <email>")
        sys.exit(1)

    url = sys.argv[1]
    email = sys.argv[2]

    try:
        payload = {'email': email}
        r = requests.post(url, data=payload)
        print(r.text)
    except requests.RequestException as e:
        print("Error accessing the URL: {}".format(e))
