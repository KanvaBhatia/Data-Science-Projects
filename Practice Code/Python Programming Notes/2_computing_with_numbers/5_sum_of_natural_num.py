"""
    #  5_sum_of_natural_num.py
    # This program find the sum of the first n natural numbers
    Created by: temikelani on: 1/25/20
"""
def natural_sum():
    print("This program find the sum of the first n natural numbers: ")
    # asks user for input
    n = int(input("Please enter value for n: "))
    sum = 0

    for i in range(1, n+1):
        sum += i;

    print(sum)

natural_sum()