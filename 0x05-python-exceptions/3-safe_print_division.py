#!/usr/bin/python3

def safe_print_division(a, b):
    """Returns a the division of two numbers

    Args:
        a (_int_): _description_
        b (_int_): _description_

    Returns:
        _int/float_: _description_
    """
    try:
        results = a / b
    except ZeroDivisionError:
        results = None
    finally:
        print("Inside results: {}".format(results))
    return results
