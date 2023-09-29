#!/usr/bin/python3
""" This module implements conventional way of handling requests """
if __name__ == "__main__":
    from sys import argv
    from urllib import request, error

    try:
        with request.urlopen(argv[1]) as res:
            if res.getcode() == 200:
                print(res.read().decode("utf-8"))
    except error.HTTPError as err:
        print(f"Error code: {err.status}")
