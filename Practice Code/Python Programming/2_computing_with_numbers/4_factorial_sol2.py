"""
    # 4_factorial_sol2.py
    # This program calculates the factorial of a number provided by the user
    Created by: temikelani on: 1/25/20
"""

def factorial():
    print("This program calculates the factorial of a number provided by you")
    num = int(input("Enter number here: "))
    factorial = num

    for i in range(num-1, 1, -1):
        factorial *= i

    print(num, "! is: ", factorial)


factorial()
