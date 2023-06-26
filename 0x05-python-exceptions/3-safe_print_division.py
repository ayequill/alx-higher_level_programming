#!/usr/bin/python3

def safe_print_division(a, b):
    """Returns a the division of two numbers

    Args:
        a (_int_): _description_
        b (_int_): _description_

    Returns:
        _int/float_: _description_
    """
    results = 0
    try:
        results = a / b
    except (ZeroDivisionError, TypeError):
        results = None
    finally:
        print("Inside results: {}".format(results))
    return results
