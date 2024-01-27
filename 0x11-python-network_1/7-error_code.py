#!/usr/bin/python3
"""
a Python script that takes in a URL, sends a request
to the URL and displays the body of the response.
"""
import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]

    response = requests.get(url)

    if response.status_code >= 400:
        # print the status error code
        print("Error code:", response.status_code)
    else:
        # print the body of the response
        print(response.text)
