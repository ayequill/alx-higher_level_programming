#!/usr/bin/python3
""" This module prints out a specific header key """
from urllib import request
from sys import argv

with request.urlopen(argv[1]) as response:
    if response.getcode() == 200:
        print(response.getheader("X-Request-Id"))
