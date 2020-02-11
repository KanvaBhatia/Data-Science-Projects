"""
    # 2_print_month.py
    # A program to print the abbreviation of a month, given its number without any decision structures
    Created by: temikelani on: 1/27/20
"""

def print_month():
    print("This program will print the abbreviation of a month, given its number \n")
    # collect month num from user
    num = int(input("Please enter the month number here: "))

    # set the var months to be a string of all the months (3-letter) abbreviations concatenated together
    # each new moth will hold a positions +3 places from previous one 0 = Jan, 3 = Feb etc.
    months = "JanFebMarAprMayJunJulAugSepOctNovDec"

    # this var converts number entered to position of string. 1 = 0, 2 = 3, 3 = 6 etc...
    position = (num - 1) * 3

    # print the abbreviatiosn
    print("That month is: ", months[position:position+3])

print_month()