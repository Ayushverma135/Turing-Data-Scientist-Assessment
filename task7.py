import pandas as pd
from data_loader import load_data

def host_attribute_with_second_highest_correlation_to_reviews(df_listings):
    # Clean and convert relevant columns
    df_listings['host_is_superhost'] = df_listings['host_is_superhost'].map({'t': 1, 'f': 0}).fillna(0).astype(int)
    df_listings['host_identity_verified'] = df_listings['host_identity_verified'].map({'t': 1, 'f': 0}).fillna(0).astype(int)
    
    # Select relevant columns and drop rows with missing values in these columns
    relevant_columns = [
        'number_of_reviews', 'host_since', 'host_listings_count', 
        'host_identity_verified', 'calculated_host_listings_count', 'host_is_superhost'
    ]
    df_listings = df_listings[relevant_columns].dropna()
    
    # Convert 'host_since' to a numerical value representing the number of days since the host joined
    df_listings['host_since'] = pd.to_datetime(df_listings['host_since'])
    df_listings['host_since'] = (pd.Timestamp.now() - df_listings['host_since']).dt.days
    
    # Calculate correlations with 'number_of_reviews'
    correlations = df_listings.corr()['number_of_reviews']
    
    # Find the host attribute with the second strongest correlation
    sorted_correlations = correlations.abs().sort_values(ascending=False)
    result = sorted_correlations.index[1]  # The second strongest correlation

    return result

# Explain your solution in plain english here
"""
1. Load the data and clean the 'host_is_superhost' and 'host_identity_verified' columns by mapping 't' and 'f' to 1 and 0, and fill missing values with 0.
2. Convert the 'host_since' column to a numerical value representing the number of days since the host joined.
3. Select the relevant columns and drop rows with missing values to ensure accurate calculations.
4. Calculate the correlation between each host attribute and the 'number_of_reviews' column.
5. Identify the host attribute with the second strongest absolute correlation to the 'number_of_reviews' and return its name.
"""

# Comments End
if __name__ == '__main__':
    df_listings = load_data('path_to_listings.csv')  # Load your data using the load_data function from data_loader module
    print('Host attribute with second highest correlation to reviews is:', host_attribute_with_second_highest_correlation_to_reviews(df_listings))
