#!/usr/bin/python3
"""Fetches the 'X-Request-Id' header from a specified URL."""
import urllib.request
import sys


if __name__ == "__main__":
    """This script takes a URL as a command-line argument and attempts
    to fetch the 'X-Request-Id' header from the HTTP response. If found,
    it prints the 'X-Request-Id' value; otherwise, it notifies that
    the header was not found in the response.

    Usage:
        python3 1-htbn_header.py <URL>

    Arguments:
        URL (str): The URL from which to fetch the 'X-Request-Id' header.

    Example:
        $ python3 1-htbn_header.py https://example.com
        12345

    Note:
        - This script requires Python 3.
        - It uses urllib.request to send an HTTP request and retrieve
          the 'X-Request-Id' header.
    """
    if len(sys.argv) < 2:
        print("Usage: ./1-htbn_header.py <URL>")
        sys.exit(1)

    url = sys.argv[1]

    try:
        with urllib.request.urlopen(url) as response:
            x_request_id = response.getheader('X-Request-Id')
            if x_request_id:
                print(x_request_id)
            else:
                print("X-Request-Id header not found in the response.")
    except urllib.error.URLError as e:
        print("Error accessing the URL: {}".format(e))
