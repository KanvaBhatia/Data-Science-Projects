"""
    # 3_life_exp_histograms.py
    # Exploring life expectancy with histograms
    Created by: temikelani on: 2/10/20
"""

import pandas as pd
import matplotlib.pyplot as plt

# read date about countries
countries = pd.read_csv("Datasets/gapminder.csv")

# create a list containing the life expectancy
life_exp = countries.life_exp

# Build histogram. try 5, 15 and 20 bins
plt.hist(life_exp, bins=5)
plt.xlabel("Life Expectancy [in years]")
plt.show()

plt.clf()

plt.hist(life_exp, bins=15)
plt.xlabel("Life Expectancy [in years]")
plt.show()

plt.clf()

plt.hist(life_exp, bins=20)
plt.xlabel("Life Expectancy [in years]")
plt.show()