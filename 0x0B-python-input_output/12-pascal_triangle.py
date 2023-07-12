#!/usr/bin/python3
"""a module which define a function
which implements a pascal triangle"""


def pascal_triangle(n):
    """pascal triangle implementation
    Args:
    n(int): number
    """
    if n <= 0:
        return []
    my_list = []
    for i in range(n):
        l1 = []
        for j in range(i + 1):
            if j == 0 or j == i:
                l1.append(1)
            else:
                l1.append(l2[j] + l2[j - 1])
        l2 = l1
        my_list.append(l1)
    return my_list
