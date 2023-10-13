#!/usr/bin/python3
# a function that returns a key with the biggest integer value.


def best_score(a_dictionary):
    max_val = 0
    if not a_dictionary:
        return (None)
    for key, value in a_dictionary.items():
        if max_val <= a_dictionary[key]:
            max_val = a_dictionary[key]
            new_key = key
    return (new_key)
