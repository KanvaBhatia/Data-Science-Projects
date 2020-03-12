"""
    # 2_max_of_three
    #
    Created by: temikelani on: 2/3/20
"""


def max_of_three(x1, x2, x3):
    # make a list to contain all values
    values = [x1, x2, x3]

    # var max_val holds the largest value but currently holds the value of the first input
    max_val = x1
    for i in values:
        if i > max_val:
            max_val = i

    return max_val


def main():
    print("This program returns the maximum of three ")

    x1 = float(input("Enter first num: "))
    x2 = float(input("Enter second num: "))
    x3 = float(input("Enter third num: "))

    print("the largest number is", max_of_three(x1, x2, x3))

main()
