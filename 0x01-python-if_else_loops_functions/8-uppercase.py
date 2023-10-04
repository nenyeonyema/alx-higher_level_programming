#!/usr/bin/python3
def uppercase(a):
    for char in a:
        if 'a' <= char <= 'z':
            uppercase_char = chr(ord(char) - 32)
        else:
            uppercase_char = char
        print("{}".format(uppercase_char), end="")
    print()
