#!/usr/bin/python3
if __name__ == "__main__":
    numOfArgs = len(sys.argv) - 1
    if numOfArgs == 0:
        print("{:d} arguments.".format(numOfArgs))
    elif numOfArgs == 1:
        print("{:d} argument:".format(numOfArgs))
    else:
        print("{:d} arguments:".format(numOfArgs))
    for i in range(1, numOfArgs + 1)
        print("{:d}: {:s}".format(i, sys.argv[i]))
