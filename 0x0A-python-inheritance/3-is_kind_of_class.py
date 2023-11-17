#!/usr/bin/python3
"""Class Inheritance"""


def is_kind_of_class(obj, a_class):
    """
    a function that checks if an object is an
    instance or inherited instance of a class.
    Parameters:
        obj (any): The object to check.
        a_class (type): The class to match the type of obj to.
    Returns:
    True if the object is an instance or inherited instance of a_class,
    otherwise False.
    """
    if isinstance(obj, a_class):
        return True
    else:
        False
