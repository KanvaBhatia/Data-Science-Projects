"""
 # 4_exploring_vehicle_data
    # Exploring vehicle data in 7 countries, using car per capita and side of road driven on
    # using pandas, numpy boolean operators, logical_and etc
    Created by: temikelani on: 2/11/20
"""

import pandas as pd
import numpy as np

# Import cars data
cars = pd.read_csv('Datasets/cars.csv', index_col=0)

# Print cars
print("\n 0 \n", cars)

# Extract drives_right column as Dataframe: sel
sel = cars[cars["drives_right"]]

# Print sel
print("\n 1. drives right \n", sel)

# Create car_maniac: observations that have a cars_per_cap over 500
car_maniac = cars[cars["cars_per_cap"] > 500]

# Print car_maniac
print("\n 2. per cap > 500 \n", car_maniac)

# Create medium: observations with cars_per_cap between 100 and 500
medium = cars[np.logical_and(cars["cars_per_cap"] > 100, cars["cars_per_cap"] < 500)]

# Print medium
print("\n 2 per cap (100-500) \n", medium)
