#!/usr/bin/python3

# Check if URL is provided as an argument
if [ $# -ne 1 ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

# Assign URL from command-line argument
URL=$1

# Send request using curl and capture response body size
response=$(curl -sI "$URL" | grep -i "Content-Length" | awk '{print $2}')

# Display the size of the response body in bytes
if [ -z "$response" ]; then
    echo "Failed to retrieve content size. Please check if the URL is correct."
else
    echo "Response body size: $response bytes"
fi
