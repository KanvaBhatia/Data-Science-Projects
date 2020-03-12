# 2_average_score.py
# This program finds the average of 3 scores, supplied by the user
# Created by: temikelani on: 1/24/20

print("This program find the average of 3 exam scores")

def average():
    # simultaneously collects and assigns scores to variables
    score1, score2, score3 = eval(input("Enter 3 scores separated by commas: "))
    average = (score1 + score2 + score3) / 3
    print("the Average is: ", average)

average()