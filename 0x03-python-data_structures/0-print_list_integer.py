#!/usr/bin/python3
def print_list_integer(my_list=[]):
    if my_list is None:
        my_list = []
    for item in range(len(my_list)):
        print("{}".format(item))
