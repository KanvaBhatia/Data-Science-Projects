"""
    # 3_change_counter.py
    # This program accepts the count of each type of coin and provides the sum
    Created by: temikelani on: 1/25/20
    # Future plans: Could make it simultaneous entry // for that you need eval())
"""


def count_change():
    print("This program accepts the count of each type of coin and provides the sum")
    # asks use to provide count
    quarters = int(input("Enter number of quarters: "))
    dimes = int(input("Enter number of dimes: "))
    nickels = int(input("Enter number of nickels: "))
    pennies = int(input("Enter number of pennies: "))
    # evaluates and holds sum of all change rounded to 2 decimal places
    total = round((quarters * 0.25) + (dimes * 0.10) + (nickels * 0.05) + (pennies * 0.01), 2)
    print()  # blank space
    print("The total value of change is {0:0.2f}".format(total))


count_change()
