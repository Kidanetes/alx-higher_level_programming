#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    len1 = len(tuple_a)
    len2 = len(tuple_b)
    a = []
    b = []
    c = []
    for i in range(0, 2):
        if i < len1:
            a.append(tuple_a[i])
        else:
            a.append(0)
    for i in range(0, 2):
        if i < len2:
            b.append(tuple_b[i])
        else:
            b.append(0)
    for i in range(2):
        c.append(a[i] + b[i])
    d = c[0], c[1]
    return d
