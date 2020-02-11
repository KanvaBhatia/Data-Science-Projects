"""
    # 1_happy_birthday.py
    # program prints the happy birthday song with any name
    Created by: temikelani on: 1/29/20
"""


def happy():
    return "Happy birthday to you!\n"


def verse(person):
    lyrics = happy() * 2 + "Happy birthday, dear " + person + ".\n" + happy()
    return lyrics


def sing(person):
    for person in ["Ngadie", "Fran", "Me"]:
        print(verse(person))


sing("Fred")
