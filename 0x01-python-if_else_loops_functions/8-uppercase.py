#!/usr/bin/python3
def uppercase(str):
    for i in range(len(str)):
        if ord(str[i]) >= ord('a') and ord(str[i]) <= ord('z'):
            print("{:c}".format(ord(str[i]) + ord('A') - ord('a')), end="\n" if i == len(str) - 1 else "")
        else:
            print("{:c}".format(ord(str[i])), end="\n" if i == len(str) - 1 else "")
