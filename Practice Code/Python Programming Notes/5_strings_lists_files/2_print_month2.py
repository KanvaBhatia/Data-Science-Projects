"""
    # 2_print_month2.py
    # A program to print the abbreviation of a month, given its number using lists
    Created by: temikelani on: 1/27/20
"""


def main():
    # months is a list used as a lookup table
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    n = int(input("Enter a month number (1-12) : "))
    print("The month abbreviation is", months[n - 1] + ".")


main()
