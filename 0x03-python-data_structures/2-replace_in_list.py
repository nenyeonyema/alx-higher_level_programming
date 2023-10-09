#!/usr/bin/python3
#  a function that replaces an element of a list at a specific position


def replace_in_list(my_list, idx, element):
    lent = (len(my_list)-1)
    if idx < 0 or idx > lent:
        return (my_list)
    my_list[idx] = element
    return (my_list)
