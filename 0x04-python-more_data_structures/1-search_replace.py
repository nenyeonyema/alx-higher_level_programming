#!/usr/bin/python3
#  a function that replaces all occurrences of
# an element by another in a new list.


def search_replace(my_list, search, replace):
    new_list = my_list[:]

    for idx, item in enumerate(new_list):
        if item == search:
            new_list[idx] = replace
    return (new_list)
