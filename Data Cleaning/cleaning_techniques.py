import pandas as pd
from scipy import stats

# Load your dataset
df = pd.read_csv("your_dataset.csv")

# 1. Removing Null Values
# Remove rows with any null values
cleaned_df = df.dropna()

# Remove columns with any null values
cleaned_df = df.dropna(axis=1)

# Remove rows where specific columns have null values
cleaned_df = df.dropna(subset=['column1', 'column2'])

# 2. Imputation (Filling Missing Values)
# Fill null values with a specific value
df['column'].fillna(value, inplace=True)

# Fill null values with the mean of the column
mean_value = df['column'].mean()
df['column'].fillna(mean_value, inplace=True)

# Forward fill null values with the last valid observation
df['column'].fillna(method='ffill', inplace=True)

# Backward fill null values with the next valid observation
df['column'].fillna(method='bfill', inplace=True)

# 3. Data Type Conversion
# Convert string columns to datetime
df['date_column'] = pd.to_datetime(df['date_column'])

# Convert numeric columns to integers or floats
df['numeric_column'] = df['numeric_column'].astype(int)
df['numeric_column'] = df['numeric_column'].astype(float)

# 4. Removing Duplicates
# Remove duplicate rows
cleaned_df = df.drop_duplicates()

# Remove duplicate rows based on specific columns
cleaned_df = df.drop_duplicates(subset=['column1', 'column2'])

# 5. String Cleaning
# Remove leading and trailing whitespace
df['text_column'] = df['text_column'].str.strip()

# Convert text to lowercase
df['text_column'] = df['text_column'].str.lower()

# Replace characters or substrings
df['text_column'] = df['text_column'].str.replace('old_value', 'new_value')

# 6. Handling Outliers
# Identify and remove outliers using z-score
z_scores = stats.zscore(df['numeric_column'])
df = df[(z_scores < 3)]

# Identify and remove outliers using IQR (Interquartile Range)
Q1 = df['numeric_column'].quantile(0.25)
Q3 = df['numeric_column'].quantile(0.75)
IQR = Q3 - Q1
df = df[~((df['numeric_column'] < (Q1 - 1.5 * IQR)) | (df['numeric_column'] > (Q3 + 1.5 * IQR)))]

# Save cleaned data to a new file
cleaned_df.to_csv("cleaned_data.csv", index=False)
