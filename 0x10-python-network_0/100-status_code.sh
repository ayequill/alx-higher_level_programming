#!/bin/bash
# Display only the status code
curl -sI "$1" | head -n1 | awk -F ' ' '{print $2}'