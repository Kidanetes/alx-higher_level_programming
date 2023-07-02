#!/usr/bin/python3
"""this module contains a function which
will divide a matrix by integer
"""


def matrix_divided(matrix, div):
    """a function which will divide a matrix
    by a constant number
    Args:
    matrix(list): a list which contains other lists
    div(int or float): a number will will divide the matrix
    return: a new matrix
    """
    if type(matrix) is not list:
        raise TypeError(('matrix must be a matrix '
                        '(list of lists) of integers/floats'))
    for i in matrix:
        if type(i) is not list:
            raise TypeError(('matrix must be a matrix '
                            '(list of lists) of integers/floats'))
        for k in i:
            if type(k) is not int and type(k) is not float:
                raise TypeError(('matrix must be a matrix '
                                '(list of lists) of integers/floats'))
    for i in range(len(matrix)):
        if i != 0:
            if len(matrix[i]) != len(matrix[i - 1]):
                raise TypeError('Each row of the matrix '
                                'must have the same size')
    if not(type(div) is int or type(div) is float):
        raise TypeError('div must be a number')
    if div == 0:
        raise ZeroDivisionError('division by zero')
    new_matrix = []
    for i in matrix:
        k = []
        for j in i:
            k.append((int((j / div) * 100)) / 100)
        new_matrix.append(k)
    return new_matrix
