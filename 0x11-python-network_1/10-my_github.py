#!/usr/bin/python3
""" Sends a get request with error handling """
from sys import argv
from requests import get, exceptions

if __name__ == "__main__":
    user, token = argv[1], argv[2]
    headers = {
        "Authorization": f"Bearer {token}"
    }
    response = get(f"https://api.github.com/users/{user}",
                   headers=headers)
    if response.status_code == 200:
        print(response.json().get('id'))
    else:
        print(None)
