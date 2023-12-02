#!/usr/bin/python3
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: ./5-hbtn_header.py <URL>")
        sys.exit(1)

    url = sys.argv[1]

    try:
        r = requests.get(url)
        x_request_id = r.headers.get('X-Request-Id')

        if x_request_id:
            print(x_request_id)
        else:
            print("X-Request-Id header not found in the response.")
    except requests.RequestException as e:
        print(f"Error accessing the URL: {e}")
