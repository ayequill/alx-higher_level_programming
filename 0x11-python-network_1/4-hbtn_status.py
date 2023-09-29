#!/usr/bin/python3
""" This module sends a GET request to an endpoint """
if __name__ == "__main__":
    from requests import get
    from sys import argv

    response = get(argv[1])

    if response.status_code == 200:
        data = response.json()
        print(data)
