#!/usr/bin/python3
""" This module makes a GET request and prints the data """

from urllib import request

url = 'https://alx-intranet.hbtn.io/status'
__type: str = "type: "
__content: str = "content: "
__content_utf: str = "utf8 content: "

with request.urlopen(url) as response:
    if response.getcode() == 200:
        content = response.read()
        __type += str(type(content))
        __content += str(content)
        __content_utf += str(content.decode("utf-8"))

print(f"Body response:\n    - {__type}\n    - {__content}\n"
      f"    - {__content_utf}")
