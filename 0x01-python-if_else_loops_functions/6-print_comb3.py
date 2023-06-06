#!/usr/bin/python3
for i in range(1, 100):
    if i <= 89:
        if i // 10 >= i % 10:
            continue
        if i // 10 == 8 and i % 10 == 9:
            print("{}{}".format(i // 10, i % 10), end="\n")
        else:
            print("{}{}".format(i // 10, i % 10), end=", ")
