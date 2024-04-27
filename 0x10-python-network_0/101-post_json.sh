#!/bin/bash
# Sends a JSON POST request to a URL with the contents of a file

if [ $# -ne 2 ]; then
    echo "Usage: $0 URL JSON_FILE"
    exit 1
fi

URL=$1
JSON_FILE=$2

# Check if the JSON file is valid
if ! jq empty $JSON_FILE > /dev/null 2>&1; then
    echo "Not a valid JSON"
    exit 1
fi

# Send the POST request and display the response body
curl -sX POST -H "Content-Type: application/json" --data-binary "@$JSON_FILE" "$URL"
