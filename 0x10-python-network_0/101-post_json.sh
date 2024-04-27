#!/bin/bash
# Sends a JSON POST request to a URL and displays the body of the response
if [ -f "$2" ]; then
    curl -s -X POST -H "Content-Type: application/json" -d @"$2" "$1"
else
    echo "Not a valid JSON"
fi
