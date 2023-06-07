#!/usr/bin/python3
for i in range(122, 96, -1):
    if i % 2 == 0:
        letter = i
    else:
        letter = i + ord('A') - ord('a')
    print("{:c}".format(letter), end="")
