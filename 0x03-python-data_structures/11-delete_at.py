#!/usr/bin/python3
# a function that deletes the item at a specific position in a list.


def delete_at(my_list=[], idx=0):
    lent = len(my_list)
    if idx >= 0 and idx < lent:
        del my_list[idx]
    return (my_list)
