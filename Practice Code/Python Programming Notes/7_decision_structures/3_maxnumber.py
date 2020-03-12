"""
    # 3_max_number.py
    # finds the max number in a list of numbers
    Created by: temikelani on: 2/3/20
"""


def max_num():
    numbers = input("Please enter numbers separated by space: ").split(" ")
    max_val = int(numbers[0])

    for i in numbers[1:]:
        max_val = max(max_val, int(i))
        print(max_val)

    return max_val


def main():
    print("This program returns the value of largest number in a list of numbers\n ")
    print("the largest number is:", max_num())


main()
