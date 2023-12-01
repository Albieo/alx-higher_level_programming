#!/usr/bin/python3
import subprocess
import sys


def get_response_body(url):
    command = f"curl -s -f -L {url}"
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    
    if result.returncode == 0:
        print(result.stdout.strip())
    else:
        print(None)


if __name__ == "__main__":
    url = sys.argv[1]
    get_response_body(url)