#!/bin/bash
# This script sends a GET request to the provided URL using curl
curl -s -o /tmp/response -w "%{http_code}" "$1" | { read code; if [ $code -eq 200 ]; then cat /tmp/response; fi; }
