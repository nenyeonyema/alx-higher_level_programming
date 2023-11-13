#!/usr/bin/python3
"""a function that divides all elements of a matrix."""


def matrix_divided(matrix, div):
    """a function that divides all elements of a matrix."""

    for row in matrix:
        for column in row:
            if not isinstance(column, (int or float)):
                raise TypeError("matrix must be a matrix (list of lists)\
                        of integers/floats")

    for row in matrix:
        if len(row) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = []
    for row in matrix:
        new_row = []
        for column in row:
            result = round(column / div, 2)
            new_row.append(result)
        new_matrix.append(new_row)
    return new_matrix
