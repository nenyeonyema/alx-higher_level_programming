#!/usr/bin/python3


def complex_delete(a_dictionary, value):
    new_values = [va for va in a_dictionary.values()]

    for key, val in a_dictionary.items():
        if val in new_values:
            del a_dictionary[key]
    return (a_dictionary)
