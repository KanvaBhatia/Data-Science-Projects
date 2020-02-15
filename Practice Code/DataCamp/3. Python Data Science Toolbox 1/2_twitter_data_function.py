"""
    # 2_twitter_data_function.py
    # In this exercise, you will define a function with the functionality you developed in the previous exercise,
    return the resulting dictionary from within the function, and call the function with the appropriate arguments.
    Created by: temikelani on: 2/15/20
"""

# Import pandas
import pandas as pd

# Import Twitter data as DataFrame: df
tweets_df = pd.read_csv('Datasets/tweets.csv')
print(tweets_df.info())


def count_entries(d_frame, col_name):
    # Initialize an empty dictionary: item_count
    item_count = {}

    # Extract column from DataFrame: col
    col = d_frame[col_name]

    # Iterate over lang column in DataFrame
    for entry in col:

        # If the language is in item_count, add 1/
        # this is the check in dictionary syntax
        if entry in item_count.keys():
            item_count[entry] += 1
        # Else add the language to item_count, set the value to 1
        else:
            item_count[entry] = 1

    # Return the item_count dictionary
    return item_count

# Call the function count_entries
result = count_entries(tweets_df, 'lang')

print(result)