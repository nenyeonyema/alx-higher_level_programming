#!/bin/bash
# This script sends a request to the specified URL
response=$(mktemp) && curl -s -o "$response" -w "%{http_code}" "$1" && status_code=$(cat "$response") && echo "$status_code" && rm "$response"
