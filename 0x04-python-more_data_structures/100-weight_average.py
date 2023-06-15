#!/usr/bin/python3

def weight_average(my_list=[]):
    if not my_list:
        return 0
    product_of_tuple = 0
    sum_of_tuple = 0
    for x, y in my_list:
        product_of_tuple += x * y
        sum_of_tuple += y
    return product_of_tuple / sum_of_tuple
