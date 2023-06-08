#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    x = len(argv) - 1
    if x == 0:
        print("{} arguments.".format(x), end="\n")
    elif x == 1:
        print("{} argument:".format(x), end="\n")
        print("1: {}".format(argv[1]), end="\n")
    else:
        print("{} arguments:".format(x), end="\n")
        for i in range(1, x):
            print("{}: {}".format(i, argv[i]), end="\n")
