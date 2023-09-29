#!/usr/bin/python3
""" This script makes a POST request to an endpoint """
from sys import argv
from urllib.request import Request, urlopen
from urllib.parse import urlencode

url, data = argv[1], urlencode({'email': argv[2]}).encode("utf-8")

req = Request(url, data=data)

with urlopen(req) as response:
    print(response.read().decode("utf-8"))
