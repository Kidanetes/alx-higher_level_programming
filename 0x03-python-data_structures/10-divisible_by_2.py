#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    numOfElements = len(my_list)
    if numOfElements == 0:
        return None
    a = []
    for i in range(numOfElements):
        if my_list[i] % 2 == 0:
            a.append(True)
        else:
            a.append(False)
    return a
