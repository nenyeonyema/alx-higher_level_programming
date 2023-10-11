#!/usr/bin/python3
# a function that adds all unique integers
# in a list (only once for each integer).


def uniq_add(my_list=[]):
    unique_set = set()
    total = 0
    for item in my_list:
        if my_list.count(item) == 1 and item not in unique_set:
            total += item
            unique_set.add(item)
    for item in my_list:
        if my_list.count(item) >= 1 and item not in unique_set:
            total += item
            unique_set.add(item)
    return (total)
