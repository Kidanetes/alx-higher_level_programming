#!/usr/bin/python3
def no_c(my_string):
    strlen = len(my_string)
    str = ""
    for i in range(strlen):
        if my_string[i] != 'c' and my_string[i] != 'C':
            str = str + my_string[i]
    return str
