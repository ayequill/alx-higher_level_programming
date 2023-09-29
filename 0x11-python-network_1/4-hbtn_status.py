#!/usr/bin/python3
""" This module sends a GET request to an endpoint """
if __name__ == "__main__":
    from requests import get
    from sys import argv

    response = get("https://alx-intranet.hbtn.io/status")

    if response.status_code == 200:
        data = response.text
        print(f"Body response:\n\t: {type(data)}\n\tent: {data}")
        print(type(data))
