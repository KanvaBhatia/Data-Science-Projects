"""
    # 2_pop_vs_life_expectancy.py
    # exploring the correlation between life expectancy and the population of different countries
    Created by: temikelani on: 2/10/20
"""


import pandas as pd
import matplotlib.pyplot as plt

# read date about countries
countries = pd.read_csv("Datasets/gapminder.csv")

# create lists containing the life expectancy and population of the countries
life_exp = countries.life_exp
pop = countries.population

# Build Scatter plot
plt.scatter(pop, life_exp)
plt.xlabel("Population")
plt.ylabel("Life Expectancy [in years]")
plt.show()
