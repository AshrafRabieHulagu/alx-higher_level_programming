#!/bin/bash
# JSON post with curl
curl -sH "Content-Type: application/json" -X POST -d @"$2" "$1"
