"""
    # 7_name_value.py
    # The value of a name is determined by summing up the values of the letters of the name
    # where "a" is # 1' "b" is 2' "c" is 3' up to "z" being 26.
    # For example' the name "Zelle"  # would have the value 26 + 5 + 12 + 12 + 5 = 60
    # Write a program that calculates the numeric value of a single name provided as input.
    #
    Created by: temikelani n: 1/28/20
"""


def main():
    print("this program calculated the numerical value of your name: ")

    # name is split to eliminate spaces and stored in a list. list is then converted back to string
    name = input("Please enter your first name: ").split(" ")
    name_str = "".join(name)
    lcase_name = name_str.lower()  # ensures all characters are in lowe case

    # holds the total name value
    nameValue = 0

    # using ASCII a=97 and z=122. therefor to make a = 1 as required we use  # (ASCII(a) - 96)
    # and do the same for all letters
    for i in lcase_name:
        nameValue += (ord(i) - 96)

    print("\n The value of your name is:", nameValue)


main()
