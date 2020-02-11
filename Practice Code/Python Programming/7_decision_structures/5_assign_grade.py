"""
    # 5_assign_grade.py
    # A professor gives 100-point exams that are graded on the scale 90-100:A, 80-89:B, 70-79:C, 60-69:D, <60:F.
    # Write a program that accepts an exam score as input and prints out the corresponding grade.
    Created by: temikelani on: 2/3/20
"""


def grade(score):
    if score < 60:
        print("Grade is F")
    elif 60 <= score <= 69:
        print("Grade is D")
    elif 70 <= score <= 79:
        print("Grade is C")
    elif 80 <= score <= 89:
        print("Grade is B")
    else:
        print("Grade is A")


def main():
    print("This program tells you your grade\n")
    grade(float(input("Enter your score here: ")))


main()
