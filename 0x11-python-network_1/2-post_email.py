#!/usr/bin/python3
"""
This script sends a POST request to a specified URL with an email parameter.
"""
import urllib.request
import urllib.parse
import sys


if __name__ == "__main__":
    """
    Usage:
        python3 2-post_email.py <URL> <email>

    Args:
        URL (str): The URL to which the POST request will be sent.
        email (str): The email address to be sent as a parameter in
        the request.

    Example:
        $ python3 2-post_email.py http://example.com/submit user@example.com

    The script uses the `urllib.request` module to encode the email
    parameter and sends a POST request to the specified URL. It catches
    `URLError` exceptions if there are issues accessing the URL and prints
    an error message.
    """
    if len(sys.argv) < 3:
        print("Usage: ./2-post_email.py <URL> <email>")
        sys.exit(1)

    url = sys.argv[1]
    email = sys.argv[2]

    data = urllib.parse.urlencode({'email': email}).encode('utf-8')
    req = urllib.request.Request(url, data=data, method='POST')

    try:
        with urllib.request.urlopen(req) as response:
            body = response.read().decode('utf-8')
            print(body)
    except urllib.error.URLError as e:
        print("Error accessing the URL: {}".format(e))
