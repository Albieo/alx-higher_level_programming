#!/usr/bin/python3
import subprocess
import sys


def get_response_size(url):
    command = f"curl -s -o /dev/null -w '%{{size_download}}' {url}"
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    
    if result.returncode == 0:
        print(f"Size of the response body in bytes: {result.stdout.strip()}")
    else:
        print("Error occurred while fetching response size.")


if __name__ == "__main__":
    url = sys.argv[1]
    get_response_size(url)