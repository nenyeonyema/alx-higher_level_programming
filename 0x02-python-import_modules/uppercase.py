#!/usr/bin/python3


def print_alphabet(n=65):
    print(chr(n), end='')
    if n == 90:
        print('')
    else:
        print_alphabet(n+1)
