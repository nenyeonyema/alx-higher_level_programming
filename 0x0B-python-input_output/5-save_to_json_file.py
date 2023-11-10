#!/usr/bin/python3
"""
a function that writes an Object to a text file,
using a JSON representation
"""
import json


def save_to_json_file(my_obj, filename):
    """writes an Object to a text file, using JSON representation"""
    with open("filename", 'w') as fn:
        json.dump(my_obj, fn)
