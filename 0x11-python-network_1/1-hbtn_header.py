#!/usr/bin/python3
"""
Write a Python script that takes in a URL, sends a request to the URL and 
displays the value of the X-Request-Id variable found in 
the header of the response.
"""
import urllib.request
import sys


if __name__ == "__main__":
    # Get URL from command line argument
    url = sys.argv[1]
    # Send request and handle response
    with urllib.request.urlopen(url) as response:
        # Check if 'X-Request-Id' exists in the response headers
        if 'X-Request-Id' in response.headers:
            # Display the value of 'X-Request-Id' variable
            print(response.headers['X-Request-Id'])
        else:
            print("X-Request-Id not found in response headers.")