#!/usr/bin/python3
def uppercase(str):
    for i in range(len(str)):
        if ord(str[i]) >= ord('a') and ord(str[i]) <= ord('z'):
            letter = str[i]) + ord('A') - ord('a')
        else:
            letter = str[i]
        print("{:c}".format(letter))
    print("")
