"""
    # 4_exploring_vehicle_data
    # Manipulating vehicle data in 7 countries, using car per capita and side of road driven on
    # using pandas and dictionaries
    Created by: temikelani on: 2/10/20
"""

import pandas as pd

# Collect vehicle data from csv
cars = pd.read_csv("Datasets/cars.csv", index_col=0)

# Assign columns to lists
names = cars.country  # country names
dr = cars.drives_right  # drives right or not
cpc = cars.cars_per_cap  # cars per capita

# Create dictionary my_dict with three key:value pairs: my_dict
my_dict = {"country": names, "drives_right": dr, "cars_per_cap": cpc}

# Turn my_dict into a DataFrame called cars2
cars2 = pd.DataFrame(my_dict)
cars2.index = ["US", "AUS", "JAP", "IN", "RU", "MOR", "EG"]

print("\n", cars2)
print("\n", cars)  # for comparison
