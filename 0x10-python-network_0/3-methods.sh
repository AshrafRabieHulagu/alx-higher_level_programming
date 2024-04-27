#!/bin/bash
# Displays all HTTP methods the server will accept for a URL
curl -sI "$1" | grep -i "Allow" | cut -d' ' -f2-
