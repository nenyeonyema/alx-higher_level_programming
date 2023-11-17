#!/usr/bin/python3
# a function that returns the weighted average of all integers tuple (<score>, <weight>)
# edited from putty

def weight_average(my_list=[]):
    if not my_list:
        return (0)
    weight = numera = denom  = 0
    idx = 1
    for item in my_list:
        for i in item:
            if i == my_list[0][1]:
                denom += i
            idx *= i
        numera += idx
    weight = numera / denom
    return (weight)
