#!/usr/bin/python3
""" Sends a POST request """
if __name__ == "__main__":
    from sys import argv
    from requests import post

    response = post(argv[1], data={'email': argv[2]})
    if response.status_code == 200:
        print(response.text)
