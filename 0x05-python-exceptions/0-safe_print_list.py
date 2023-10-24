#!/usr/bin/python3
# a function that prints x elements of a list


def safe_print_list(my_list=[], x=0):
    count = 0

    for item in my_list:
        try:
            print(item, end="")
            count += 1

            if count >= x:
                break
        except IndexError:
            pass

    print("")
    return (count)
