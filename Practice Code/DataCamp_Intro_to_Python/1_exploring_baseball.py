"""
    # 1_exploring_baseball.py
    # Practice with Numpy arrays
    Created by: temikelani on: 2/6/20
"""

import numpy as np
import pandas as pd

# Read baseball dataset
b_ball = pd.read_csv("Datasets/baseball.csv")
# print(b_ball)

# Assign player heights in inches to a variable
height_in = b_ball["Height"]
# print(height_in)

# Create numpy array from height_in and convert to meters
np_height_m = np.array(height_in) * 0.0254
# print(np_height_m)

# Assign player weights in lb to a variable
weight_lb = b_ball["Weight"]
# print(weight_lb)

# Create numpy array from weight_lb and convert to kg
np_weight_kg = np.array(weight_lb) * 0.453592
# print(np_weight_kg)

# Calculate BMI
bmi = np_weight_kg / np_height_m ** 2
# print(bmi)

# Create a boolean np array that with its elements true if bmi < 21
light = bmi < 21

# Print out BMIs of all baseball players with BMIs < 21
# print(bmi[light])

# Print out the weight at index 50
# print(np_weight_kg[50])

# Print out sub-array of np_height_m: index 100 up to and including index 110
# print(np_height_m[100:111])


