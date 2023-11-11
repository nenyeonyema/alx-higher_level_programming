#!/usr/bin/python3
""" a class Student that defines a student """


class Student:
    """Represent a student."""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ get a dictionary representation of the Student"""
        return self.__dict__
