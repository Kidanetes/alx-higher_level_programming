#!/usr/bin/python3
def magic_calculation(a, b):
    import magic_calculation_102 as x
    if a < b:
        result = x.add(a, b)
        for i in range(4, 6):
            result = x.add(result, i)
        return result
    else:
        return x.sub(a, b)
