#!/usr/bin/python3
# a function that returns a new dictionary with all values multiplied by 2


def multiply_by_2(a_dictionary):
    new_dict = a_dictionary.copy()
    for key, value in new_dict.items():
        new_dict.update({key: value * 2})
    return (new_dict)
