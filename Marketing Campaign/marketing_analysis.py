import pandas as pd

# Load the dataset from a CSV file
df = pd.read_csv('marketing_campaign.csv', sep='\t', 
                   index_col='ID', 
                   parse_dates=['Dt_Customer'])

# Display the first few rows of the DataFrame
print(df.head(10))

# Check for missing values in each column
missing_values = df.isnull().sum()
print("Missing values in each column:")
print(missing_values)

df.info()
print(df['Z_Revenue'].value_counts())
print(df['Z_CostContact'].value_counts())

df.drop(columns=['Z_Revenue', 'Z_CostContact'], inplace=True)



# Handle missing values appropriately (e.g., by imputation or removal)
# For example, if you want to fill missing values with the mean of the column:
# df.fillna(df.mean(), inplace=True)

# Or if you want to remove rows with missing values:
# df.dropna(inplace=True)

# You can choose the appropriate method based on your dataset and analysis goals
