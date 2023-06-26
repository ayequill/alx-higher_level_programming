#!/usr/bin/python3


def search_replace(my_list, search, replace):
    """_summary_

    Args:
        my_list (_list_): _list with numbers_
        search (_number_): _element to be replaced_
        replace (_number_): _new element_

    Returns:
        _list_: _new list with replaced value_
    """
    return list(map(lambda element: replace if
                    search == element else element, my_list))
