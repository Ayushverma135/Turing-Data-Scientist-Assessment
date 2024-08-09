# src/task6.py
import pandas as pd

# Load the data
listings = pd.read_csv('path_to_listings.csv')

# Group by superhost status and calculate average review scores
average_scores = listings.groupby('host_is_superhost')['review_scores_rating'].mean()

# Calculate the difference
average_difference = average_scores[True] - average_scores[False]

print(average_difference)
