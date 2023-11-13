#!/usr/bin/python3
"""prints a text with 2 new lines """


def text_indentation(text):
    """
     a function that prints a text with 2 new lines after
     each of these characters: ., ? and :
     Parameter:
     - text (str): a string of charcacters
     Raises:
     TypeError: text must be a string
     """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    new_string = ""
    for char in text:
        new_string += char
        if char in ['.', ':', '?']:
            print(new_string.strip())
            print()
            new_string = ""

    if new_string:
        print(new_string.strip())
