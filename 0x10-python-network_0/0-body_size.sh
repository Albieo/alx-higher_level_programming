#!/bin/bash
# a Bash script that takes in a URL, sends a request to that URL,
#    and displays the size of the body of the response

# Check if a URL is provided as an argument
if [ $# -eq 0 ]; then
    echo "Please provide a URL as an argument."
    exit 1
fi

# Get the URL from the argument
URL=$1

# Get the size of the response body in bytes
if size=$(curl -s -o response.txt -w "%{size_download}" "$URL"); then
    echo "$size"
else
    echo "Failed to retrieve the response."
fi

# Clean up - remove the temporary file
rm -f response.txt