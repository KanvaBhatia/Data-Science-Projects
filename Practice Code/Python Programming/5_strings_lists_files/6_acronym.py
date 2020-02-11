"""
    # 6_acronym.py
    # Write a program that allows the user to type in a phrase and then outputs the acronym for that phrase.
    # Note: The acronym should be all uppercase, even if the words in the phrase are not capitalized.
    # For example, RAM is an acronym for "random access memory."
    Created by: temikelani on: 1/28/20
"""


def main():
    print("This program generates an abbreviation!")
    # collect user's phrase nd capitalise the first letter of each word
    phrase = input("Please enter phrase: ").title()

    # make a list to contain phrase when split by spaces
    phrase_list = phrase.split(" ")

    # Collect first letter: abbr will hold abbreviation
    abbr = ""

    # count to total length of items in list
    for i in range(len(phrase_list)):
        for j in phrase_list[i]:
            abbr += j
            break
    print("\n The abbreviation is:", abbr)


main()
