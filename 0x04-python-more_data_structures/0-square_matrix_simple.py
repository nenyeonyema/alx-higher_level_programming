#!/usr/bin/python3
# a function that computes the square value of all integers of a matrix.


def square_matrix_simple(matrix=[]):
    new_matrix = []
    for row in matrix:
        new_row = []
        for column in row:
            new_row.append(column ** 2)
        new_matrix.append(new_row)
    return (new_matrix)

