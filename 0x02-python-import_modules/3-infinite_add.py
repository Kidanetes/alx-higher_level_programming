#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    sum = 0
    numOfArgs = len(sys.argv) - 1
    if numOfArgs == 0:
        print(sum)
    else:
        for i in range(1, numOfArgs + 1):
            sum = sum + int(sys.argv[i])
        print(sum)
