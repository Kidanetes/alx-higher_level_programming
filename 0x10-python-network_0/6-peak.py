#!/usr/bin/python3
"""find a peak from a list"""


def find_peak(list_of_integers):
    """find a peak from a list
    Argument:
    list_of_integers(list)
    """
    if len(list_of_integers) == 0:
       return None
    list_of_integers.sort() 
    return list_of_integers[-1]
