#!/bin/bash
# Makes a request to 0.0.0.0:5000/catch_me to get the response "You got me!"

# Send a PUT request with custom header to cause the server to respond with "You got me!"
curl -sX PUT -H "Origin: HolbertonSchool" -d "user_id=98" 0.0.0.0:5000/catch_me
