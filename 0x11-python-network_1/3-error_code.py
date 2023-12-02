#!/usr/bin/python3
""" Script to retrieve content from a provided URL and handle HTTP errors. """
import urllib.request
import sys


if __name__ == "__main__":
    """
    Usage Example:
        ./3-error_code.py <URL>

    Args:
        URL (str): The URL to retrieve content from.

    Description:
        This script takes a URL as an argument and attempts to fetch
        its content. If successful, it prints the content to the console.
        If an HTTPError occurs (e.g., 404, 500), it catches the error and
        prints the corresponding error code.

    Example:
        $ ./3-error_code.py https://www.example.com
        HTML content of the provided URL
        $ ./3-error_code.py https://www.invalidurl.com
        Error code: 404

    Note:
        Requires Python 3.x and the 'urllib' module.
    """

    if len(sys.argv) < 2:
        print("Usage: ./3-error_code.py <URL>")
        sys.exit(1)

    url = sys.argv[1]

    try:
        with urllib.request.urlopen(url) as response:
            body = response.read().decode('utf-8')
            print(body)
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
