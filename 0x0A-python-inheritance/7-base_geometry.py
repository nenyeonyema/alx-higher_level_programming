#!/usr/bin/python3
"""Class inheritance"""


class BaseGeometry:
    """ a class based geometry"""
    def area(self):
        """ area not implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ validate the integer <value>"""
        self.name = name
        self.value = value

        if not isinstance(value, int):
            raise TypeError("<name> must be an integer")
        if value <= 0:
            raise ValueError("<name> must be greater than 0")
