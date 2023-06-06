#!/usr/bin/python3
x = 97
while x < 97 + 26:
    if chr(x) in "eq":
        x = x + 1
        continue
    print("{:c}".format(x), end="")
    x = x + 1
