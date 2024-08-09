import pandas as pd
from data_loader import load_data

def neighbourhood_with_highest_median_price_diff(df_listings):
    # Clean the price column by removing '$' and ',' and convert it to float
    df_listings['price'] = df_listings['price'].replace('[\$,]', '', regex=True).astype(float)
    
    # Group by neighborhood and host_is_superhost, then calculate the median price
    grouped = df_listings.groupby(['neighbourhood_cleansed', 'host_is_superhost'])['price'].median().unstack(fill_value=0)
    
    # Calculate the difference between superhosts and non-superhosts
    grouped['difference'] = grouped.get(True, 0) - grouped.get(False, 0)
    
    # Find the neighborhood with the largest difference
    result = grouped['difference'].idxmax()
    
    return result

# Explain your solution in plain english here
"""
1. Load the data and clean the 'price' column by removing '$' and ',' symbols, and convert it to float for numerical operations.
2. Group the data by 'neighbourhood_cleansed' and 'host_is_superhost', then calculate the median price for each group.
3. Handle cases where there might not be any superhosts or non-superhosts in a neighborhood by filling missing values with 0.
4. Calculate the price difference between superhosts and non-superhosts for each neighborhood.
5. Identify the neighborhood with the largest median price difference and return its name.
"""

# Comments End
if __name__ == '__main__':
    df_listings = load_data('path_to_listings.csv')  # Load your data using the load_data function from data_loader module
    print('Neighborhood with highest price difference:', neighbourhood_with_highest_median_price_diff(df_listings))
