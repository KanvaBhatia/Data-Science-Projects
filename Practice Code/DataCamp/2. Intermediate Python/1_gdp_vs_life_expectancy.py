"""
    # 1_gdp_vs_life_expectancy.py
    # exploring the correlation between life expectancy an gdp/capita of different countries
    Created by: temikelani on: 2/10/20
"""

import pandas as pd
import matplotlib.pyplot as plt

# read date about countries
countries = pd.read_csv("Datasets/gapminder.csv")

# create lists containing the life expectancy and gdp of the countries
life_exp = countries.life_exp
gdp_cap = countries.gdp_cap

# Make a scatter plot, gdp_cap on the x-axis, life_exp on the y-axis
plt.scatter(gdp_cap, life_exp)
plt.xlabel("GDP Per Capita [in USD]")
plt.ylabel("Life Expectancy [in years]")
plt.title("World Development in 2007 [143 Countries]")

# A correlation will become clear when you display the GDP per capita on a logarithmic
# Put the x-axis on a logarithmic scale
plt.xscale("log")

# Customise x-ticks
plt.xticks([1000, 10000, 100000], ["1k", "10k", "100k"])

# Display the plot
plt.show()
