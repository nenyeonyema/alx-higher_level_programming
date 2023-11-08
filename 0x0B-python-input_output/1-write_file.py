#!/usr/bin/python3
"""
a function that writes a string to a text file (UTF8)
and returns the number of characters written
"""


def write_file(filename="", text=""):
    """
    a function that writes a string to a text file UTF8

    Parameters:
    - filename (string): a text file
    - text (string): a string literal

    Returns:
    int: the number of characters written
    """
    with open(filename, mode='w', encoding="utf-8") as newfile:
        output = newfile.write(text)
        return output
