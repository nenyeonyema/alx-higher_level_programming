#!/usr/bin/python3
""" Class inheritance"""


class BaseGeometry:
    """Public instance method that raises an exception"""
    def area(self):
        """ Class Not implemented"""
        raise Exception("area() is not implemented")
