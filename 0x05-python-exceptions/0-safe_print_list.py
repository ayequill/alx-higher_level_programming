#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    """_summary_

    Args:
        my_list (list, optional): _description_. Defaults to [].
        x (int, optional): _description_. Defaults to 0.

    Returns:
        _number_: _length of items in list_
    """
    len_of_list: int = 0
    for index in range(x):
        try:    
            print("{}".format(my_list[index]), end="")
            len_of_list += 1
        except (IndexError):
            break
    print()
    return len_of_list
