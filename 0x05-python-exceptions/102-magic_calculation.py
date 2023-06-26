#!/usr/bin/python3
def magic_calculation(a, b):
    j = 0
    for i in range(1, 3):
        try:
            if i > a:
                raise Exception('Too far')
            else:
                j = j + a**b / i
        except Exception:
            j = a + b
            break
    return j
