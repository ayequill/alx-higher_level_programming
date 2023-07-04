#!/usr/bin/python3
"""
A locked class
"""


class LockedClass:
    """
    A restricted class that prevents dynamic creating
    of new
    instance if the name is not defined __slots__
    """
    __slots__ = ("first_name")
