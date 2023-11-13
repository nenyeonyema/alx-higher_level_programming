#!/usr/bin/python3
"""prints a square"""



def print_square(size):
    """
    a function that prints a square with the character #.
    Parameter:
    - size (int): size of the square

    Raises:
    TypeError: size must be an integer
    ValueErrror: size must be >= 0
    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")

    for row in range(size):
        print("#" * size)
