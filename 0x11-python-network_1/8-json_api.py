#!/usr/bin/python3
import requests
import sys


if __name__ == "__main__":
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
