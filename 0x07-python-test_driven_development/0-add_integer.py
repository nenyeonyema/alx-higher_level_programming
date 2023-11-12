#!/usr/bin/python3
""" a function that adds two integer """


def add_integer(a, b=98):
    """
    a function that adds two integer.
    Parameters:
        a (int): expects an int argument.
        b (int): expects an int arguement.
    Returns:
        The addition of a and b, if float arguments
        are received, they re both typecasted to an int
        before addition is performed.
    Raises:
        TypeError: if none of the arguments is either an int or float.
    """

    if not (isinstance(a, int) or isinstance(a, float)):
        raise TypeError("a must be an integer")
    if not (isinstance(b, int) or isinstance(b, float)):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))

# print(add_integer.__doc__)
