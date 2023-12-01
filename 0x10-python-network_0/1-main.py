#!/usr/bin/python3
import subprocess
import sys


def get_response_body(url):
    command = f"curl -s -o response.txt -w '%{{http_code}}' {url}"
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    
    if result.returncode == 0:
        http_code = result.stdout.strip()
        if http_code == '200':
            with open('response.txt', 'r') as file:
                body = file.read()
                print(f"Body of the response (Status Code 200):\n{body}")
        else:
            print(f"Non-200 status code received: {http_code}")
    else:
        print("Error occurred while fetching the response body.")

if __name__ == "__main__":
    url = sys.argv[1]
    get_response_body(url)