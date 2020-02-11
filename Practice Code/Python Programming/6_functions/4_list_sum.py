"""
    # 4_list_sum.py
    # Write and test a function to meet this specification.
    # sumList(nums) nums is a list of numbers. Returns the sum of the numbers in the list.
    Created by: temikelani on: 1/30/20
"""


def createList():
    # asks user for values to enter into list. entry is stored (as strings) in a list
    list = input("please enter integers separates by commas (x,y,z etc):").split(",")
    # empty list to hold int values of list (list)
    list_int = []
    # converting entries in list to int and storing them in list_int
    for i in list:
        list_int.append(int(i))
    return list_int


def sum(list):
    sum = 0
    for i in list:
        sum += i
    return sum


def main():
    print("The sum of the list is:", sum(createList()))


main()
