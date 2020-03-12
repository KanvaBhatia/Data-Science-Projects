"""
    # 5_assign_grade.py
    # A professor gives 100-point exams that are graded on the scale 90-100:A, 80-89:B, 70-79:C, 60-69:D, <60:F.
    # Write a program that accepts an exam score as input and prints out the corresponding grade.
    Created by: temikelani on: 1/28/20
"""


def main():
    # generate list of grades. each representing
    # 0-9,10-19,20-29,30-39,40-49,50-59,60-69,70-79,80-89,90-99,100
    grades = ["F", "F", "F", "F", "F", "F", "D", "C", "B", "A", "A"]

    # collect score from user
    score = int(input("Please enter your score here (1-100): "))

    # grade is calculated using integer division
    # if score is 10, then 10//10 is 1 which is assign to grades[1]
    print("Your grade is:", str(grades[score // 10]) + ".")


main()
