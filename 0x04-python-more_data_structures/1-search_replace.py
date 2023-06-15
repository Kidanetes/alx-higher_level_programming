#!/usr/bin/python3
def search_replace(my_list, search, replace):
    len1 = len(my_list)
    a = []
    for i in range(len1):
        if my_list[i] == search:
            a.append(replace)
        else:
            a.append(my_list[i])
    return a
