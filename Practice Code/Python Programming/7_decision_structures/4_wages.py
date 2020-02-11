"""
    # 4_wages.py
    # Program calculates weekly pay based on total hours. Overtime pay begins at 40+ hours
    Created by: temikelani on: 2/3/20
"""


def wages(hours, rate):
    if hours > 40:
        return (40 * rate) + ((hours - 40) * (1.5 * rate))
    else:
        return hours * rate


def main():
    print("This program calculates the weekly pay based on the total hours and rate per hour\n")
    hours = float(input("Enter hours spent working: "))
    rate = float(input("Enter rate per hour: "))

    print("\n Your wage is", wages(hours, rate))


main()
