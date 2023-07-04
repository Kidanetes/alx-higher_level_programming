#!/usr/bin/python3
"""this module contains two functions
the first function checks if the matrix
is legit, the second one multiplies the marices
"""


def matrix_check(matrix, name):
    """this function checks if a matrix
    ful fils all the criteria
    Args:
    matrix(list): the matrix
    name(str): name of the matrix
    """
    if type(matrix) is not list:
        raise TypeError('{} must be a list'.format(name))
    for i in matrix:
        if type(i) is not list:
            raise TypeError('{} must be a list of lists'.format(name))
        for k in i:
            if type(k) is not int and type(k) is not float:
                raise TypeError(('{} should contain'
                                ' only integers or floats').format(name))
    if len(matrix) == 0:
        raise ValueError("{} can't be empty".format(name))
    if len(matrix[0]) == 0:
        raise ValueError("{} can't be empty".format(name))
    for i in range(len(matrix)):
        if i != 0:
            if len(matrix[i]) != len(matrix[i - 1]):
                raise TypeError(('each row of {} must be'
                                ' of the same size').format(name))


def matrix_mul(m_a, m_b):
    """this function multiplies two matrices
    Args:
    m_a(list): matrix 1
    m_b(list): matrix 2
    returns: the product matrix
    """
    matrix_check(m_a, "m_a")
    matrix_check(m_b, 'm_B')

    if (len(m_a[0]) != len(m_b)):
        raise ValueError("m_a and m_b can't be multiplied")
    a = []
    for i in range(len(m_a)):
        b = []
        for j in range(len(m_b[0])):
            c = 0
            for k in range(len(m_a[0])):
                c += m_a[i][k] * m_b[k][j]
            b.append(c)
        a.append(b)
    return a
