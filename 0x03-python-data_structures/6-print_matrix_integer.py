#!/usr/bin/python3
# a function that prints a matrix of integers.


def print_matrix_integer(matrix=[[]]):
    lent =  len(matrix)

    for row in matrix:
        for column in row:
            if column != row[-1]:
                print("{:d}".format(column), end=" ")
            else:
                print("{:d}".format(column), end="")
        print()
