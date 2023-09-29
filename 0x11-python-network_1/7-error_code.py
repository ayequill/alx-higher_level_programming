#!/usr/bin/python3
""" Sends a get request with error handling """
from sys import argv
from requests import get, exceptions

try:
    response = get(argv[1])
    response.raise_for_status()
except exceptions.RequestException as e:
    print(f"Error code: {response.status_code}")
else:
    print(response.text)
