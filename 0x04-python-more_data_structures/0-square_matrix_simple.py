#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    """_summary_

    Args:
        matrix (list, optional): _description_. Defaults to [].

    Returns:
        _list_: _description_
    """
    if len(matrix) == 0:
        return []
    # new_matrix = []
    # for i in matrix:
    #     new_matrix.append((list(map(lambda x: x**2, i))))
    # return new_matrix
    return list(map(lambda sublist:
                    list(map(lambda x: x**2, sublist)), matrix))
