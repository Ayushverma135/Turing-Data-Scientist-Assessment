# Turing-Data-Scientist-Assessment
![turing](https://github.com/user-attachments/assets/f92719f1-c65e-4d5c-8c47-2d0b4aa32b94)

## Problem Statement
You are provided with a dataset containing vacation rental listings and reviews. Your task is to complete the code in seven separate Python task files, each addressing a specific question using the provided dataset.

## Dataset description:
This dataset contains two files:

• **Listings:** This is a table that contains information about the vacation rental listings in a city. Every listing has a single row in the table and contains several attributes related to the listing as well as the host for the listing.

• **Reviews:** This is a table that contains information about all the guest reviews for the listings in the "Listings" table, along with related attributes as the date of the review and the reviewer name.

## Task 1: Neighborhood Price Difference

What is the neighborhood in which superhosts have the biggest median price difference with respect to non superhosts? Use the following three columns in the 'listings' dataset to answer this question: 'host_is_superhost', 'neighbourhood_cleansed', and 'price'. [Difficulty: Medium]

**Example:**
```python3 src/task1.py```

## Task 2: Correlation Analysis

Which of the review scores has the strongest correlation to price? Use the following review score columns in the 'listings' dataset 'review_scores_rating'. 'review_scores_accuracy', 'review_scores_cleanliness', 'review_scores_checkin'. review_scores_communication', 'review_scores_location', 'review_scores_value' [Difficulty: Easy]

**NB: Correlation strength can be either positive or negative**

**Example:**
```python3 src/task2.py```

## Task 3: Professional Host Analysis

What is the average price difference between a professional host and a non- professional one? Consider a host as professional if they have listings in more than 5 different locations (location is defined by the 'neighbourhood_cleansed column). [Difficulty: Medium]

**Example:**
```python3 src/task3.py```

## Task 4: Median Price Premium

What is the median price premium given to entire homes/ entire apartments with respect to other listings of the same neighborhood? Report the average across all neighborhoods. Use the 'room_type' column in the 'listings' dataset to distinguish between entire homes / entire apartments and other types of listings. [Difficulty: Medium]

**Example:**
```python3 src/task4.py```

## Task 5: Best Listing for Revenue

What is the listing with the best expected revenue based on the last 12 months, considering 60% of guests leave reviews and every guest will stay only the minimum number of nights? Use both the 'listings' and 'reviews' datasets for this question and only use listings with minimum nights of stay <= 7 The 'minimum_nights' column Indicates the required minimum number of nights of stay for any listing. [Difficulty: Medium]

**Example:**
```python3 src/tasks.py```

## Task 6: Average difference of review scores

What is the average difference between review scores of superhosts vs normal hosts? Use the 'review_scores_rating' column for determining the average review scores.
[Difficulty: Easy]

**Example:**
```python3 src/task6.py```

## Task 7: Second strongest correlated host attribute with number of reviews

Which host attribute has the second-strongest correlation with the number of reviews of the listing? Use the following columns as the host attributes host since host listings_count', 'host identity_verified', 'calculated_host_listings_count host_is_superhost', Use 'number_of_reviews' as the column to find correlation with [Difficulty: Medium]

**NB: Correlation strength can be either positive or negative**

**Example**
```python3 src/task7.py```
