#!/usr/bin/python3
""" Sends a POST request with parameters """
from sys import argv
from requests import post

q = "" if len(argv) < 2 else argv[1]
url = f"http://0.0.0.0:5000/search_user"

try:
    response = post(url, data={'q': q})
    data = response.json()
except ValueError:
    print('Not a valid JSON')
else:
    print(f"[{data['id']}] {data['name']}"
          if data else "No result")
