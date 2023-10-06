#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    len_args = len(argv) - 1  # Subtract 1 to exclude the script name itself
    args = argv[1:]  # Exclude the script name from the list

    if len_args == 0:
        print(int("0"))
    result = 0
    for items in args:
        result = result + int(items)
    print("{}".format(result))
