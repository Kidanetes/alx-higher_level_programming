#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv, exit
    from calculator_1 import add, sub, mul, div
    num = len(argv) -  1
    if num != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>", end="\n")
        exit(1)
    else:
        a = int(argv[1])
        b = int(argv[3])
        op = argv[2]
        if op == "+":
            print("{} {} {} = {}".format(a, op, b, add(a, b)), end="\n")
        elif op == "-":
            print("{} {} {} = {}".format(a, op, b, sub(a, b)), end="\n")
        elif op == "*":
            print("{} {} {} = {}".format(a, op, b, mul(a, b)), end="\n")
        elif op == "/":
            print("{} {} {} = {}".format(a, op, b, div(a, b)), end="\n")
        else:
            print("Unknown operator. Available operators: +, -, * and /", end="\n")
            exit(1)
    exit(0)
