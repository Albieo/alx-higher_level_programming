#!/usr/bin/python3
"""This script retrieves the 'X-Request-Id' header
from a given URL using the requests module."""
import requests
import sys


if __name__ == "__main__":
    """
    Usage:
        python3 5-hbtn_header.py <URL>

    Arguments:
        <URL>: The URL from which to retrieve the 'X-Request-Id' header.

    Example:
        python3 5-hbtn_header.py https://example.com

    Upon execution, this script sends a GET request to the provided
    URL and prints the 'X-Request-Id' header value if found in
    the response. If the header is not present, it displays a message
    indicating its absence. In case of any errors during the request,
    it will print an error message.
    """
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
        print("Error accessing the URL: {}".format(e))
