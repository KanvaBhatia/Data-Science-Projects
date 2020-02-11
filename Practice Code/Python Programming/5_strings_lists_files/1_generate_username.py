"""
    # 1_generate_username.py
    # This program creates a username from the initials (firstname) and first 7 letters (of last name)
    # a user provides
    Created by: temikelani on: 1/27/20
"""


def username():
    print("This program generates a username! \n")
    # collect user's first and last name
    first = input("Please enter first name (all lowercase): ")
    last = input("Please enter last name (all lowercase): ")

    # concatenate initial of first name with first 7 characters of last name
    usrname = first[0] + last[:7]
    print("Your username is: ", usrname)


username()
