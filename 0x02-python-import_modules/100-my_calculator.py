#!/usr/bin/python3
if __name__ == '__main__':
    from calculator_1 import add, sub, div, mul
    import sys
    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    op = ["+", "-", "*", "/"]
    a = int(sys.argv[1])
    op_s = sys.argv[2]
    b = int(sys.argv[3])
    fun = [add, sub, mul, div]
    for i in range(len(op)):
        if op[i] == op_s:
            print("{} {} {} = {}".format(a, op_s, b, fun[i](a,b)))
            sys.exit(0)
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
