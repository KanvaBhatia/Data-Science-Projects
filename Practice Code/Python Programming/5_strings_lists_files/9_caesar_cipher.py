"""
    # 9_caesar_cipher.py
    # This program builds a caesar cipher that shifts each letter by a key
    # For example, if the key value is 2, the word "Sourpuss" would be encoded as "Uqwtrwuu."
    # A true Caesar cipher does the shifting in a circular fashion where the next character after "z" is "a."
    # assuming all letters are lowercase, and phrase only consists of letters and phrases
    Created by: temiKelani on: 1/28/20
"""


def main():
    print("This program encodes & decodes a phrase using a key(max 1-26)",
          "\n (only lowercase letters and spaces, no characters) : ")
    print("E.g. if the key value is 2, the word 'Sourpuss' would be encoded as 'Uqwtrwuu'")

    # user provides phrase and key:
    phrase = input("Please enter phrase: ")
    key = int(input("Please enter key: "))
    lcase_name = phrase.lower()  # ensures all characters are in lower case

    # the position of each letter represents it's value (1-26) and (27-52)
    # a dummy value "dummy is use to hold the position 0.
    # alphabet is repeated to create circular effect of going from z to a and back. max value of key is 26
    letter_value = ["dummy", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r",
                    "s",
                    "t", "u", "v", "w", "x", "y", "z",
                    "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
                    "u", "v", "w", "x", "y", "z"]

    # ENCRYPTION

    encrypted_phrase = ""  # holds encrypted string

    # from ASCII, a=97 and z=122 >>> to make a = 1 as required by letter_value[index]
    # we use (ASCII(a) - 96) and do the same for all letters after applying the key
    for i in lcase_name:
        encrypted_phrase += letter_value[(ord(i) + key) - 96]

    print("\n The encrypted phrase is :", encrypted_phrase)

    # DECRYPTION

    decrypted_phrase = ""  # holds decrypted string
    for i in encrypted_phrase:
        decrypted_phrase += letter_value[(ord(i) - key) - 96]

    print("\n The encrypted phrase is :", decrypted_phrase)


main()
