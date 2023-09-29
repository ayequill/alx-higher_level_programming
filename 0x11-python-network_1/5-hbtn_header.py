#!/usr/bin/python3
""" Displays the value of a header response """
if __name__ == "__main__":
    from sys import argv
    from requests import get

    response = get(argv[1])

    if response.status_code == 200:
        print(response.headers.get('X-Request-Id'))
