"""
    # 2_sums.py
    #  Program retruns the sum and the sum of the cubes of the first n natural numbers
    # User provides  value of n
    Created by: temikelani on: 1/30/20
"""


def sumNatural(n):
    sum = 0
    for i in range(1, n + 1):
        sum += i
    return sum


def sumCubeNatural(n):
    sum = 0
    for i in range(1, n + 1):
        sum += (i**3)
    return sum


def main():
    print("This program finds the sum and the sum of the cubes of the first n natural numbers: ")
    # asks user for input
    n = int(input("Please enter value for n: "))
    print("The sum of the first", n, "numbers is:", sumNatural(n))
    print("The sum of the cubes of the first", n, "numbers is:", sumCubeNatural(n))


main()
