#!/usr/bin/python3
#  a function that finds the biggest integer of a list.


def max_integer(my_list=[]):
    if not my_list:
        return None

    max_num = my_list[0]
    for item in my_list:
        if item > max_num:
            max_num = item
    return (max_num)
