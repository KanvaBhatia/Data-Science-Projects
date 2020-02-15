"""
    # 1_exploring_baseball_2D.py
    # Practice with 2D Numpy arrays
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

# Assign player weights in lb to a variable
weight_lb = b_ball["Weight"]
# print(weight_lb)

# Make a list of lists, where each sublist represents the height and weight of a single baseball player
# new_list = []
# for i, j in zip(height_in, weight_lb):
#     new_list.append([i, j])

# make an array where each sublist represents the height and weight of a single baseball player
np_baseball = np.column_stack((height_in, weight_lb))
# print(np_baseball)
print("\n 1 \n", np_baseball.shape)

# Print out the 50th row of np_baseball
print("\n 2 \n", np_baseball[49, :])

# Select the entire second column of np_baseball: np_weight_lb
np_weight_lb = np_baseball[:, 1]

# Select the entire first column of np_baseball: np_weight_lb
np_height_in = np_baseball[:, 0]

# Print out height of 124th player
print("\n 3 \n", np_baseball[123, 0])

# Print out the mean of np_height_in
print("\n 4 \n", np.mean(np_height_in))

# Print out the median of np_height_in
print("\n 5 \n", np.median(np_height_in))

print("\n 6 \n", np_height_in)

for i in np.nditer(np_baseball):
    print("\n test \n", i)