#!/usr/bin/python3
from sys import stderr as err


def safe_function(fct, *args):
    try:
        return fct(*args)
    except Exception as e_msg:
        print(f"Exception: {e_msg}", file=err)
        return None
