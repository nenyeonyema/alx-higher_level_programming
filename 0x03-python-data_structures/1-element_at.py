#!/usr/bin/python3


def element_at(my_list, idx):
    lent = len(my_list)

    for item in range(lent):
        if idx == -(item):
            return None
        if idx > lent:
            return None
        if idx == item:
            return "{:d}".format(my_list[item])
