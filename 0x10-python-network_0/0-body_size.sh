#!/bin/bash

# Check if the script is provided with the correct number of arguments
if [ "$#" -ne 1 ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

# Send a request to the URL using curl and store the response body in a temporary file
response_body=$(mktemp)
curl -s "$1" -o "$response_body"

# Calculate the size of the response body in bytes
body_size=$(stat -c %s "$response_body")

# Display the size of the response body
echo "$body_size"

# Clean up the temporary file
rm "$response_body"
