#!/usr/bin/python3
def max_integer(my_list=[]):
    numOfElements = len(my_list)
    if numOfElements == 0:
        return None
    my_list.sort()
    return my_list[-1]
