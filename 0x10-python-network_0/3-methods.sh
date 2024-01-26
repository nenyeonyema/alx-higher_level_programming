#!/bin/bash
# This script sends an OPTIONS request to the specified URL
curl -sI "$1" | awk '/Allow/ {print substr($0, index($0,$2))}'
