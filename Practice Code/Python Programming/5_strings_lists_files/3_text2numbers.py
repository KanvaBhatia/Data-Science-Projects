"""
    # 3_text2numbers.py
    # A program to convert a textual message into a sequence of numbers, utilizing the underlying Unicode encoding.
    Created by: temikelani on: 1/27/20
"""


def main():
    print("This program converts a textual message into a sequence")
    print("of numbers representing the Unicode encoding of the message.\n")

    # Collect message to encode
    message = input("Please enter the message to encode: ")

    for ch in message:
        print(ord(ch), end=" ")


main()
