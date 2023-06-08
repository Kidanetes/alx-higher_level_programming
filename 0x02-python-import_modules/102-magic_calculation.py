#!/usr/bin/python3
def magic_calculation(a, b):
    import magic_calculation_102 as mg
    if a < b:
        res = mg.add(a, b)
        for i in range(4, 6):
            res = mg.add(res, i)
        return res
    else:
        return mg.sub(a, b)
