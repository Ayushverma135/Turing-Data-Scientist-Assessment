import pandas as pd
from data_loader import load_data

def review_score_with_highest_correlation_to_price(df_listings):
    # Clean the price column by removing '$' and ',' and convert it to float
    df_listings['price'] = df_listings['price'].replace('[\$,]', '', regex=True).astype(float)
    
    # Select relevant columns and drop rows with missing values in these columns
    review_scores = df_listings[['price', 'review_scores_rating', 'review_scores_accuracy', 'review_scores_cleanliness', 'review_scores_checkin', 'review_scores_communication', 'review_scores_location', 'review_scores_value']].dropna()
    
    # Calculate correlation
    correlations = review_scores.corr()['price']
    
    # Find the review score with the strongest correlation to price
    result = correlations.drop('price').abs().idxmax()
    
    return result

# Explain your solution in plain english here
"""
1. Load the data and clean the 'price' column by removing '$' and ',' symbols, and convert it to float for numerical operations.
2. Select the relevant review score columns and remove any rows with missing values in these columns.
3. Calculate the correlation between each review score and the price.
4. Identify the review score with the strongest absolute correlation to the price and return its name.
"""

# Comments End
if __name__ == '__main__':
    df_listings = load_data('path_to_listings.csv')  # Load your data using the load_data function from data_loader module
    print('Review score with max correlation to price is:', review_score_with_highest_correlation_to_price(df_listings))
