#!/usr/bin/python3
# a function that prints a dictionary by ordered keys.


def print_sorted_dictionary(a_dictionary):

    for key in sorted(a_dictionary):
        value = a_dictionary[key]
        print(f"{key}: {value}")

#    sorted_dict = {key: a_dictionary[key] for key in sorted(a_dictionary)}
#    # Print the sorted dictionary
#    for key, value in sorted_dict.items():
#        print(f'{key}: {value}')
