#!/bin/bash
# This script sends a GET request to the provided URL using curl
curl -s -X GET -w "%{http_code}" "$1" -o temp.txt && \
	[[ $(cat temp.txt) == "200" ]] && cat temp.txt | tail -n +2
