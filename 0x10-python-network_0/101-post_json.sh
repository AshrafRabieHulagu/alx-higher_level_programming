#!/bin/bash

# Check for required arguments
if [ $# -ne 2 ]; then
  echo "Usage: $0 <URL> <JSON_FILE>"
  exit 1
fi

# URL and JSON file path
url="$1"
json_file="$2"

# Check if JSON file exists
if [ ! -f "$json_file" ]; then
  echo "Error: File '$json_file' does not exist"
  exit 1
fi

# Send POST request with JSON data
response=$(curl -s -X POST -H "Content-Type: application/json" -d "@$json_file" "$url")

# Check for successful response (exit code 0)
if [ $? -eq 0 ]; then
  # Display response body
  echo "$response"
else
  echo "Error: Failed to send request"
fi
