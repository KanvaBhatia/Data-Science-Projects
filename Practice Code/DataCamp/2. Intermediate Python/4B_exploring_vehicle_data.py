"""
    # 4B_exploring_vehicle_data
    # Exploring vehicle data in 7 countries, using car per capita and side of road driven on
    # using pandas(square bracket selection, Loc and iLoc)
    Created by: temikelani on: 2/10/20
"""

import pandas as pd

# Collect vehicle data from csv
cars = pd.read_csv("Datasets/cars.csv", index_col=0)

# Print out country column as Pandas Series
print("\n 1 \n ", cars["country"])

# Print out country column as Pandas DataFrame
print("\n 2 \n", cars[["country"]])

# Print out DataFrame with country and drives_right columns
print("\n 3 \n", cars[["country", "drives_right"]])

# Print out first 3 observations
print("\n 4 \n", cars[0:3])

# Print out fourth, fifth and sixth observation
print("\n 5 \n", cars[3:6])

# Print out drives_right value of Morocco
print("\n 6 \n", cars.loc[["MOR"], ["drives_right"]])
print("\n 7 \n", cars.iloc[[5], [2]])

# print df
print("\n 7.1 \n", cars)

# Print sub-DataFrame
print("\n 8 \n", cars.loc[["RU", "MOR"], ["country", "drives_right"]])
print("\n 9 \n", cars.iloc[[4, 5], [1, 2]])

# Print out drives_right column as Series
print("\n 10 \n", cars.loc[:, "drives_right"])
print("\n 11 \n", cars.iloc[:, 2])

# Print out drives_right column as DataFrame
print("\n 12 \n", cars.loc[:, ["drives_right"]])
print("\n 13 \n", cars.iloc[:, [2]])

# Print out cars_per_cap and drives_right as DataFrame
print("\n 14 \n", cars.loc[:, ["cars_per_cap", "drives_right"]])
print("\n 15 \n", cars.iloc[:, [0, 2]])

# test
print("\n 16 \n", cars.loc[:, :])
print("\n 17 \n", cars.iloc[:, [0, 2]])
