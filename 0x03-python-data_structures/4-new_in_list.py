#!/usr/bin/python3
#  a function that replaces an element in a list at a specific
# position without modifying the original list


def new_in_list(my_list, idx, element):
    new_list = my_list[:]
    lent = (len(my_list)-1)

    if idx < 0 or idx > lent:
        return (my_list)
    else:
        new_list[idx] = element
        return (new_list)
