#!/usr/bin/python3
for letter in range(97, 123):
    if letter == 101 or letter == 112:
        continue
    print("{:c}".format(letter), end="")
