#!/usr/bin/python3
"""
This module demonstrates fetching data from a given URL using
the requests library.
It provides a script that takes a URL as an argument and retrieves its content,
handling potential errors.
"""
import requests
import sys


if __name__ == "__main__":
    """
    Usage:
        python3 my_module.py <URL>

    Example:
        python3 my_module.py https://example.com
    """
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
