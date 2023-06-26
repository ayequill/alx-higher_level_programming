#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    """returns the quotient of all elements in a list

    Args:
        my_list_1 (_list_): _description_
        my_list_2 (_list_): _description_
        list_length (_int_): _description_

    Returns:
        _list_: _description_
    """
    quotient = 0
    new_list = []
    for i in range(list_length):
        try:
            quotient = my_list_1[i] / my_list_2[i]
        except (ValueError, TypeError):
            print("wrong type")
            quotient = 0
        except ZeroDivisionError:
            print("division by 0")
            quotient = 0
        except IndexError:
            print("out of range")
            quotient = 0
        finally:
            new_list.append(quotient)
    return new_list
