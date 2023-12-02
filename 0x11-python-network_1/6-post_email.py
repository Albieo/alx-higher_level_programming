#!/usr/bin/python3
"""
This script sends a POST request to a specified URL with an email payload.
"""
import requests
import sys


if __name__ == "__main__":
    """
    Command-line arguments:
        - URL: The URL where the POST request will be sent.
        - Email: The email address to include in the payload.

    Example:
        ./6-post_email.py http://example.com/submit example@email.com
    """
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
