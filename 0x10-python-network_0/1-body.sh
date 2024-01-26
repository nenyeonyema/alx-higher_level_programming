#!/bin/bash
# This script sends a GET request to the provided URL using curl
response=$(mktemp)
curl -s -X GET -w "%{http_code}" "$1" -o "$response" && [[ $(< "$response") == "200" ]] && tail -n +2 < "$response"

