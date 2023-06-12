#!/usr/bin/python3
def print_list_integer(my_list=[]):
    numOfElements = len(my_list)
    if numOfElements >= 1:
        for i in range(numOfElements):
            print("{:d}".format(my_list[i]))
