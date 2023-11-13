#!/usr/bin/python3
""" a function that prints My name is <first name> <last name>"""


def say_my_name(first_name, last_name=""):
    """
    prints My name is <first name> <last name>
    Parameters:
    - first_name (str): first name string
    - last_name (str): last_name string
    Returns:
    - first_name and last_name
    Raises:
    - TypeError: first_name must be a string or last_name must be a string
    """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    #print(f"My name is {first_name} {last_name}")
    full_name = f"My name is {first_name}"
    if last_name:
        full_name += f" {last_name}"

    print(full_name)
