#!/usr/bin/python3

from sys import argv, exit
from calculator_1 import add, sub, mul, div
if __name__ == "__main__":

    if len(argv) - 1 != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    list_of_operators = ["+", "-", "*", "/"]
    if not argv[2] in list_of_operators:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)

    def calc(a, b, operator):
        if operator == '+':
            print("{} + {} = {}".format(a, b, add(a, b)))
            return a + b
        elif operator == '-':
            print("{} - {} = {}".format(a, b, sub(a, b)))
            return a - b
        elif operator == '*':
            print("{} * {} = {}".format(a, b, mul(a, b)))
            return a * b
        elif operator == '/':
            print("{} / {} = {}".format(a, b, div(a, b)))
            return a / b

    calc(int(argv[1]), int(argv[3]), argv[2])
