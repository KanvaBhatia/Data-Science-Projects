"""
    # 5_looping_dataframes.py
    # exploring vehicle data using loops
    Created by: temikelani on: 2/11/20
"""

import pandas as pd

# Import vehicle data
cars = pd.read_csv('Datasets/cars.csv', index_col=0)

# Print cars
print("\n 0 \n", cars)

# Iterate over rows of cars
print("\n 1 \n")
for label, row in cars.iterrows():
    print("\n", label)
    print(row)

# Adapt the code in the for loop such that the output should be in the form "country: cars_per_cap"
print("\n 2 \n")
for label, row in cars.iterrows():
    print(label + ":", row["cars_per_cap"])
    print(row["country"], ":", row["cars_per_cap"])

# Use a for loop to add a new column, named COUNTRY, containing the country names (UPPERCASE) in the "country" column
# Code for loop that adds COUNTRY column
print("\n 3 \n")
for label, row in cars.iterrows():
    cars.loc[label, "COUNTRY"] = row["country"].upper()
# Print cars
print(cars)

# Add COUNTRY COLUMN using one liner with .apply(str.upper)
print("\n 4 \n")
cars["COUNTRY"] = cars["country"].apply(str.upper)

print(cars)