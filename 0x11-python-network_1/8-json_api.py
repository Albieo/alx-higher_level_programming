#!/usr/bin/python3
"""This module provides functionality to perform
a search using the requests library."""
import requests
import sys


if __name__ == "__main__":
    """
    Example:
        $ python my_module.py <query>

        This script performs a search using a POST request
        to 'http://0.0.0.0:5000/search_user'.
        It takes an optional argument <query> to search for within
        the specified URL.
        If no query is provided, it defaults to an empty string.

        Upon successful search, it prints the ID and name of the found user
        from the JSON response.
        If no result is found, it prints "No result". If the response is not
        a valid JSON format, it prints "Not a valid JSON". If there's an error
        accessing the URL, it prints the error message.
    """
    if len(sys.argv) < 2:
        q = ""
    else:
        q = sys.argv[1]

    url = 'http://0.0.0.0:5000/search_user'
    payload = {'q': q}

    try:
        r = requests.post(url, data=payload)
        try:
            json_response = r.json()
            if json_response:
                print("[{}] {}"
                      .format(json_response['id'], json_response['name']))
            else:
                print("No result")
        except ValueError:
            print("Not a valid JSON")
    except requests.RequestException as e:
        print("Error accessing the URL: {}".format(e))
