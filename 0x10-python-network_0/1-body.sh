#!/bin/bash
# Sends a GET request to the URL, and displays the body of the response only if status code is 200
curl -sL "$1"
