#!/usr/bin/python3
# a function that retrieves an element from a list


def element_at(my_list, idx):
    lent = (len(my_list)-1)

    if idx < 0:
        return None
    if idx > lent:
        return None
    else:
        return (my_list[idx])
