#!/usr/bin/python3
# a function that removes all characters c and C from a string.


def no_c(my_string):
    new_string = ""

    for item in my_string:
        if item != 'c' and item != 'C':
            new_string += item
    return (new_string)
