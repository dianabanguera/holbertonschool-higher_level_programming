#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    from sys import argv
    argv_len = len(argv) - 1
    if (argv_len != 3):
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    elif (str(argv[2]) not in ["+", "-", "*", "/"]):
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    else:
        a = int(argv[1])
        b = int(argv[3])
        if argv[2] == '+':
            print(f"{a} + {b} = {add(a,b)}")
        elif argv[2] == '-':
            print(f"{a} - {b} = {sub(a, b)}")
        elif argv[2] == '*':
            print(f"{a} * {b} = {mul(a, b)}")
        elif argv[2] == '/':
            print(f"{a} / {b} = {div(a, b)}")
