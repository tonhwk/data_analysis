import pandas as pd

# Load the dataset
df = pd.read_csv('sales_data.csv')

# Convert 'Date' column to datetime
df['Date'] = pd.to_datetime(df['Date'])


# Calculate total sales revenue by date
total_revenue_by_date = df.groupby('Date')['Price'].sum()

print(f"{total_revenue_by_date}")