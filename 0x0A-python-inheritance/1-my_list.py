#!/usr/bin/python3
"""Class Inheritance"""


class MyList(list):
    def print_sorted(self):
        """Write a class MyList that inherits from list:"""
        sort_list = sorted(self)
        print(sort_list)
