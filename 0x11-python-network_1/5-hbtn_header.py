#!/usr/bin/python3
""" Displays the value of a header response """
from sys import argv
from requests import get

response = get(argv[1])

if response.status_code == 200:
    print(response.headers['X-Request-Id'])
