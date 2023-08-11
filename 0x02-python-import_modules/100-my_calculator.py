#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
import sys


def main():
    try:
        if len(sys.argv) != 4:
            print("Usage: ./100-my_calculator.py <a> <operator> <b>")
            exit(1)
        elif sys.argv[2] not in ("+", "-", "*", "/"):
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
        else:
            a = int(sys.argv[1])
            b = int(sys.argv[3])
            if sys.argv[2] == "+":
                print(f"{a} + {b} = {add(a, b)}")
            elif sys.argv[2] == "-":
                print(f"{a} - {b} = {sub(a, b)}")
            elif sys.argv[2] == "*":
                print(f"{a} * {b} = {mul(a, b)}")
            else:
                print(f"{a} / {b} = {div(a, b)}")
            exit(0)
    except (ModuleNotFoundError):
        pass



if __name__ in "__main__":
    main()
