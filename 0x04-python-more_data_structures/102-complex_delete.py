#!/usr/bin/python3
# a function that deletes keys with a specific value in a dictionary.


def complex_delete(a_dictionary, value):
    key_del = []

#   keys_to_delete = [key for key, val in a_dictionary.items() if val == value]
    for key, val in a_dictionary.items():
        if value is val:
            key_del.append(key)

    for key in key_del:
        del a_dictionary[key]

    return (a_dictionary)
