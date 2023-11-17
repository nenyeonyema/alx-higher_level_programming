#!/usr/bin/python3
import numpy as np



def lazy_matrix_mul(m_a, m_b):
    """
    Multiplies two matrices using NumPy.

    :param m_a: First matrix
    :param m_b: Second matrix
    :return: Result of the matrix multiplication
    :raises: ValueError if matrices are not valid for multiplication
    """
    try:
        result = np.dot(m_a, m_b)
        print(result)
    except ValueError as ve:
        print(ve)
