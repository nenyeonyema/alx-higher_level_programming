#!/usr/bin/python3
#a function that retrieves an element from a list


def element_at(my_list, idx):
    lent = (len(my_list)-1)

    for item in range(lent):
        if idx < 0:
            return None
        if idx > lent:
            return None
        if idx == item:
            return "{:d}".format(my_list[idx])
