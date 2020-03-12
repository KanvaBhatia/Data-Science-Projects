"""
    # 6_average_of_input.py
    # This program finds the average of a series of numbers entered by the user
    Created by: temikelani on: 1/25/20
"""


def average():
    print("This program finds the average of a series of numbers entered by the user")
    num_count = int(input("Please enter total count of numbers you wish to enter: "))
    sum = int(input("Please enter first number here: "))


    for i in range(num_count - 1):
        sum += int(input("Enter next number here: "))
        print("sum is: ", sum)

    print("The average is ", sum/num_count)


average()