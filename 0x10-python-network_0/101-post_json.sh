#!/bin/bash
# Post jspn data via file
curl -sX POST -H 'Content-Type: application/json' -d @"$2" "$1"
