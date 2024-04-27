#!/bin/bash

# Check if both arguments are provided
if [ $# -ne 2 ]; then
    echo "Usage: $0 <URL> <filename>"
    exit 1
fi

# Read the filename and check if it exists
filename="$2"
if [ ! -f "$filename" ]; then
    echo "Error: File '$filename' not found."
    exit 1
fi

# Send the JSON data from the file as a POST request
curl -s -X POST -H "Content-Type: application/json" -d "@$filename" "$1"

# Check if the response contains valid JSON
if [ $? -eq 0 ]; then
    echo "Valid JSON"
else
    echo "Not a valid JSON"
fi
