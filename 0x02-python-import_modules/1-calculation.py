#!/usr/bin/python3

if __name__ == '__main__':
    """Perform Arithmetic operations"""

    from calculator_1 import add, sub, mul, div

    a = 10
    b = 5

    # Sum
    print("{:d} + {:d} = {:d}".format(a, b, add(a, b)))
    # Difference
    print("{:d} - {:d} = {:d}".format(a, b, sub(a, b)))
    # Product
    print("{:d} * {:d} = {:d}".format(a, b, mul(a, b)))
    # Quotient
    print("{} / {} = {}".format(a, b, div(a, b)))
