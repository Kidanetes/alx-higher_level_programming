#!/usr/bin/python3
for number in range(100):
    if number <= 98:
        print("{:d}{:d}".format(number//10, number%10), end = ", ")
    else:
        print("{:d}{:d}".format(number//10, number%10), end = "\n")
