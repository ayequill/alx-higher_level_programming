#!/usr/bin/python3
"""
Module for the pascal triangle
"""


def pascal_triangle(n):
    """
    Pascal Triangle

    Args:
        n (int): _description_

    Returns:
        list: _description_
    """
    if n <= 0:
        return []

    triangle = [[1]]
    for i in range(1, n):
        row = [1]
        prev_row = triangle[i - 1]
        for j in range(1, i):
            row.append(prev_row[j - 1] + prev_row[j])
        row.append(1)
        triangle.append(row)

    return triangle
