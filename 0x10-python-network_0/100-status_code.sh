#!/bin/bash
# Display only the status code
curl -sI -o /dev/null -w "%{http_code}" "$1"
