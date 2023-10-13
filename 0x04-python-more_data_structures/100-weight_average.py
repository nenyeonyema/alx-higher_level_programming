#!/usr/bin/python3
# a function that returns the weighted average
# of all integers tuple (<score>, <weight>)


def weight_average(my_list=[]):
    if not my_list:
        return (0)
    numera = denom = 0
    for score, weight in my_list:
        numera += score * weight
        denom += weight
    avg = numera / denom
    return (avg)
