#!/bin/bash
# This script sends a request to the specified URL
curl -s -o /tmp/response -w "%{http_code}" "$1"
cat /tmp/response && rm /tmp/response
