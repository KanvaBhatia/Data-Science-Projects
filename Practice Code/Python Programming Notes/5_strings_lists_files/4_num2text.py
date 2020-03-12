"""
    # 4_num2text.py
    # A program to convert a sequence of numbers into textual message, utilizing the underlying Unicode encoding.
    Created by: temikelani on: 1/27/20
"""


def main():
    print("This program converts a sequence of Unicode numbers into")
    print("the string of text that it represents.\n")

    # collect number sequence from user as string using input(only)
    num = input("Please enter sequence, separate each no by space: ")

    # create list message to collect decoded message
    message = []

    # num.splits will make a list of numbers in num split by spacegaps
    # run through each number, the convert them to integers
    # then convert them to letters and ass them to message
    for i in num.split():
        numvalue = int(i)
        message.append(chr(numvalue))

    text = "".join(message)
    print("\nThe decoded message is: ", text)

main()