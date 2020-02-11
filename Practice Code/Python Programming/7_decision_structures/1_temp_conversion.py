"""
    # 1_temp_conversion.py
    # This program converts temp from celsius to Fahrenheit and alerts the user if the temp is extreme
    Created by: temikelani on: 2/3/20
"""


def main():
    celsius = float(input("What is the Celsius temperature? "))
    fahrenheit = 9 / 5 * celsius + 32
    print("The temperature is", fahrenheit, "degrees Fahrenheit.")

    # Print warnings for extreme temps
    if fahrenheit >= 90:
        print("It's really hot out there. Be careful!")
    if fahrenheit <= 32:
        print("Brrrrr. Be sure to dress warmly!")


main()
