# ============================================
# STEP 1: Import libraries
# ============================================
import pandas as pd   # for working with tables of data
import numpy as np    # for numerical operations

# ============================================
# STEP 2: Load the dataset
# ============================================
df = pd.read_csv('AB_NYC_2019.csv')

print("First 5 rows:")
print(df.head())

###
# ============================================
# STEP 3: Inspect the data
# ============================================
print("\nColumn info:")
df.info()

print("\nStatistics for numeric columns:")
print(df.describe())

print("\nShape (rows, columns):", df.shape)

print("\nMissing values per column:")
print(df.isnull().sum())

# ============================================
# STEP 4: Handle missing values
# ============================================

# reviews_per_month: missing means "no reviews yet", so fill with 0 (not the average)
df['reviews_per_month'] = df['reviews_per_month'].fillna(0)

# name / host_name: fill with 'Unknown' instead of dropping the row
df['name'] = df['name'].fillna('Unknown')
df['host_name'] = df['host_name'].fillna('Unknown')

# last_review: intentionally left alone - a missing date has no honest replacement

print("\nMissing values after cleaning:")
print(df.isnull().sum())

# ============================================
# STEP 5: Fix data types and duplicates
# ============================================

# Convert last_review from text into an actual date type
df['last_review'] = pd.to_datetime(df['last_review'])

# Convert repeating text categories into 'category' type (saves memory, faster filtering)
df['neighbourhood_group'] = df['neighbourhood_group'].astype('category')
df['room_type'] = df['room_type'].astype('category')

# Check and remove duplicate rows
print("\nDuplicate rows found:", df.duplicated().sum())
df = df.drop_duplicates()

# ============================================
# STEP 6: Standardize values and handle outliers
# ============================================

# Check for inconsistent text values (uncomment the fix line below if needed)
print("\nUnique room_type values:", df['room_type'].unique())
print("Unique neighbourhood_group values:", df['neighbourhood_group'].unique())
# df['room_type'] = df['room_type'].str.strip().str.lower()

# Remove listings with price = 0 (not real rentals)
df = df[df['price'] > 0]

# Look at price stats and outliers
print("\nPrice statistics:")
print(df['price'].describe())

# Cap extreme price outliers at the 99th percentile
upper_limit = df['price'].quantile(0.99)
df = df[df['price'] <= upper_limit]
print("Upper price limit kept:", upper_limit)

# Check minimum_nights for absurd values
print("\nMinimum nights statistics:")
print(df['minimum_nights'].describe())
# Optional: cap it too, e.g. keep only listings with minimum_nights <= 30
# df = df[df['minimum_nights'] <= 30]

# ============================================
# STEP 7: Final check and save
# ============================================
print("\nFinal shape after cleaning:", df.shape)
df.info()

df.to_csv('cleaned_airbnb_nyc.csv', index=False)
print("\nCleaned file saved as cleaned_airbnb_nyc.csv")