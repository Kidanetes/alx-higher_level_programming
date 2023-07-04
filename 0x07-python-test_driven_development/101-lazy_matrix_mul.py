#!/usr/bin/python3
"""this module will contain a function
which will multiply two matrices using
NumPy
"""
import numpy


def lazy_matrix_mul(m_a, m_b):
    """multiply two matrices
    Args
    m_a(list): matrix 1
    m_b(list): matrix 2
    returns:product of matrix 1 and matrix 2
    """
    return numpy.matmul(m_a, m_b)
