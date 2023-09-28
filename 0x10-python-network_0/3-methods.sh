#!/bin/bash
# Send a curl request and displays the ALLOWED methods on the server
curl -sI -X OPTIONS "$1" | grep -i 'Allow' | awk -F ': ' '{print $2}'
