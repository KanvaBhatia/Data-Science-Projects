"""
    # 3_exploring_fifa
    # SHow that the median height of goalkeepers(GK) if higher than the median heights of other players
    Created by: temikelani on: 2/7/20
"""

import numpy as np
import pandas as pd

# Read CSV
fifa = pd.read_csv("Datasets/fifa.csv")

# collects columns of height and positions into lists
heights = fifa[" height"]  # space because through fifa.info() we see space in column name
positions = fifa[" position"]

# Make them into Numpy arrays
np_heights = np.array(heights)
np_position = np.array(positions)

# Collect heights of GKeepers
gk_heights = np_heights[np_position == " GK"]  # print(fifa[fifa[" position"] == " GK"]) with "GK" nothing shows up
print(gk_heights)

# Collect other players' heights
other_heights = np_heights[np_position != " GK"]
print(other_heights)

# print out medians
print(np.median(gk_heights))
print(np.median(other_heights))


