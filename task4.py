# src/task4.py
import pandas as pd

# Load the data
listings = pd.read_csv('path_to_listings.csv')

# Clean the price column
listings['price'] = listings['price'].replace('[\$,]', '', regex=True).astype(float)

# Separate entire homes/apartments from other types
entire_homes = listings[listings['room_type'] == 'Entire home/apt']

# Calculate the median price per neighborhood for entire homes and other types
median_price_entire = entire_homes.groupby('neighbourhood_cleansed')['price'].median()
median_price_others = listings[listings['room_type'] != 'Entire home/apt'].groupby('neighbourhood_cleansed')['price'].median()

# Calculate the premium
price_premium = median_price_entire - median_price_others

# Calculate the average premium across all neighborhoods
average_premium = price_premium.mean()

print(average_premium)
