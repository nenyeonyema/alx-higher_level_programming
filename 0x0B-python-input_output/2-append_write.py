#!/usr/bin/python3
"""
a function that appends a string at the end of a text file
(UTF8) and returns the number of characters added
"""


def append_write(filename="", text=""):
    """
     a function that appends a string at the end of a text file

    Parameters:
    - filename (string): a text file
    - text (string): string literal

    Returns:
    int: the number of characters appended
    """
    with open(filename, 'a', encoding="utf-8") as addfile:
        output = addfile.write(text)
        return output
