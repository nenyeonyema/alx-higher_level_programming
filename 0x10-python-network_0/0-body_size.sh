#!/usr/bin/python3

import sys
import requests

if len(sys.argv) != 2:
    print("Usage: {} <URL>".format(sys.argv[0]))
    sys.exit(1)

url = sys.argv[1]

try:
    response = requests.get(url)
    body_size = len(response.content)
    print(body_size)
except Exception as e:
    print("Error:", e)
    sys.exit(1)
