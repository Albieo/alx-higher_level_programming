import urllib.request
import urllib.parse
import sys


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python script.py <URL> <email>")
        sys.exit(1)

    url = sys.argv[1]
    email = sys.argv[2]

    data = urllib.parse.urlencode({'email': email}).encode('utf-8')
    req = urllib.request.Request(url, data=data, method='POST')

    try:
        with urllib.request.urlopen(req) as response:
            body = response.read().decode('utf-8')
            print(f"Response Body: {body}")
    except urllib.error.URLError as e:
        print(f"Error accessing the URL: {e}")
