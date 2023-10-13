#!/usr/bin/python3
# a function that returns a set of all elements present in only one set.


def only_diff_elements(set_1, set_2):
    diff_element = set_1 ^ set_2
    return diff_element
