#!/usr/bin/python3

def safe_print_integer(value):
    """_summary_

    Args:
        value (_int_): _description_

    Returns:
        _bool_: _description_
    """
    value_checker: bool
    try:
        print("{:d}".format(value))
        value_checker = True
        return value_checker
    except (ValueError, TypeError):
        value_checker = False
        return value_checker
