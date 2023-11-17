#!/usr/bin/python3
# a function that converts a Roman numeral to an integer.


def roman_to_int(roman_string):
    if not roman_string or None:
        return (None)
    num_bel = ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X']
    num_abv = ['XL', 'L', 'XC', 'C', 'CD', 'D', 'cM', 'M', 'MM', 'MMM']

    for i in range(1, 20):
        if roman_string in num_bel and i <= 10:
            for item in num_bel:
                item = i
    print(item)

