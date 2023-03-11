#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    numOfElements = len(my_list)
    if idx < 0:
        return my_list.copy()
    elif idx >= numOfElements:
        return my_list.copy()
    else:
        a = my_list.copy()
        a[idx] = element
        return a
