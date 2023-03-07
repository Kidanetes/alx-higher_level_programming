#!/usr/bin/python3
for letter in range(97, 123):
    if letter == 101 or letter == 111:
        continue
    print("{:c}".format(letter), end="")
