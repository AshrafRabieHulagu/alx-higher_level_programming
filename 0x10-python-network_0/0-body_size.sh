#!/bin/bash
# This script takes a URL as an argument, sends a request to that URL using curl in silent mode, and displays the size of the response body in bytes
curl -sI "$1" | grep -i "Content-Length" | awk '{print $2}'
# Check if the user provided a URL argument
if [ $# -ne 1 ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi
# Send a request to the URL and store the response body in a temporary file
response=$(curl -sI "$1")
content_length=$(echo "$response" | grep -i "Content-Length" | awk '{print $2}')
# Display the size of the response body in bytes
echo "$content_length"
