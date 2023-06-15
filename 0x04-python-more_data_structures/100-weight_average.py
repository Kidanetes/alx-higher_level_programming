#!/usr/bin/python3
def weight_average(my_list=[]):
    len1 = len(my_list)
    num = 0
    den = 0
    if len1 == 0:
        return 0
    for i in range(len1):
        num = num + my_list[i][0] * my_list[i][1]
        den = den + my_list[i][1]
    return num / den
