#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    len1 = len(a)
    len2 = len(b)
    c = ()
    if len1 < 2:
        for i in range(len1, 2):
            a = a , 0
    if len2 < 2:
        for i in range(len1, 2):
            b = b , 0
    for i in range(2):
        c = c, a[i] + b[i]
    return c
