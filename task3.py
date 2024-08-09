# src/task3.py
import pandas as pd

# Load the data
listings = pd.read_csv('path_to_listings.csv')

# Clean the price column
listings['price'] = listings['price'].replace('[\$,]', '', regex=True).astype(float)

# Count the number of unique neighborhoods per host
host_neighborhood_count = listings.groupby('host_id')['neighbourhood_cleansed'].nunique()

# Identify professional hosts
professional_hosts = host_neighborhood_count[host_neighborhood_count > 5].index

# Calculate average price for professional and non-professional hosts
average_price_professional = listings[listings['host_id'].isin(professional_hosts)]['price'].mean()
average_price_non_professional = listings[~listings['host_id'].isin(professional_hosts)]['price'].mean()

# Calculate the difference
price_difference = average_price_professional - average_price_non_professional

print(price_difference)
