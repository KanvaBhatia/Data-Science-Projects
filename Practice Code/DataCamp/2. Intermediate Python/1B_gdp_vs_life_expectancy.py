"""
    # 1B_gdp_vs_life_expectancy.py
    # Exploring the correlation between life expectancy an gdp/capita of different countries
    # 1B: Here the populations is use as size in teh scatter plot
    Created by: temikelani on: 2/10/20
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# read date about countries
countries = pd.read_csv("Datasets/gapminder.csv")

# create lists containing the life expectancy and gdp of the countries
life_exp = countries.life_exp
gdp_cap = countries.gdp_cap
pop = countries.population
np_pop = np.array(pop)      # making pop a numpy array

# Double np_pop to get enlarge the sizes of the plots
np_pop /= 1000000


# Make a scatter plot, gdp_cap on the x-axis, life_exp on the y-axis
# Set size of scatter plots to np_pop
plt.scatter(gdp_cap, life_exp, s=np_pop)
plt.xlabel("GDP Per Capita [in USD]")
plt.ylabel("Life Expectancy [in years]")
plt.title("World Development in 2007 [143 Countries]")

# Put the x-axis on a logarithmic scale
plt.xscale("log")

# Customise x-ticks
plt.xticks([1000, 10000, 100000], ["1k", "10k", "100k"])

# Display the plot
plt.show()
