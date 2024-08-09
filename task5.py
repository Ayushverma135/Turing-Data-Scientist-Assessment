# src/task5.py
import pandas as pd

# Load the data
listings = pd.read_csv('path_to_listings.csv')
reviews = pd.read_csv('path_to_reviews.csv')

# Clean the price column
listings['price'] = listings['price'].replace('[\$,]', '', regex=True).astype(float)

# Filter listings with minimum nights <= 7
listings = listings[listings['minimum_nights'] <= 7]

# Count reviews in the last 12 months
reviews['date'] = pd.to_datetime(reviews['date'])
reviews_last_12_months = reviews[reviews['date'] >= pd.Timestamp.now() - pd.DateOffset(months=12)]
review_counts = reviews_last_12_months['listing_id'].value_counts()

# Calculate the expected revenue
listings['expected_revenue'] = listings.apply(
    lambda row: row['price'] * row['minimum_nights'] * (review_counts.get(row['id'], 0) / 0.6),
    axis=1
)

# Find the listing with the highest expected revenue
best_listing_id = listings.loc[listings['expected_revenue'].idxmax()]['id']

print(best_listing_id)
