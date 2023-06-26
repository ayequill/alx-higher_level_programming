#!/usr/bin/python3

from sys import stderr as err


def safe_print_integer_err(value):
    """_summary_

    Args:
        value (_type_): _description_

    Returns:
        _type_: _description_
    """
    try:
        print("{:d}".format(value))
        return True
    except (TypeError, ValueError) as e_msg:
        print("Exception: {}".format(e_msg), file=err)
        return False
