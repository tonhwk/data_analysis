import pandas as pd

# Load the dataset
df = pd.read_csv('sales_data.csv')

# Display the first few rows of the dataset
print("First few rows of the dataset:")
print(df.head())

# Check the data types of each column
print("\nData types of each column:")
print(df.dtypes)

# Check for missing values
print("\nMissing values:")
print(df.isnull().sum())

# Summary statistics for numerical columns
print("\nSummary statistics:")
print(df.describe())

# Visualization: Sales by product
import matplotlib.pyplot as plt

# Group by product and calculate total sales
sales_by_product = df.groupby('Product')['Quantity'].sum()

# Plot bar chart
sales_by_product.plot(kind='bar', rot=0)
plt.title('Sales by Product')
plt.xlabel('Product')
plt.ylabel('Total Quantity Sold')
plt.show()

# Visualization: Proportion of sales by product
# Calculate proportion of sales
sales_proportion = df['Product'].value_counts(normalize=True) * 100

# Plot pie chart
sales_proportion.plot(kind='pie', autopct='%1.1f%%')
plt.title('Proportion of Sales by Product')
plt.ylabel('')
plt.show()

# Data analysis: Total revenue for each day
df['TotalRevenue'] = df['Price'] * df['Quantity']
total_revenue_by_date = df.groupby('Date')['TotalRevenue'].sum()
print("\nTotal revenue for each day:")
print(total_revenue_by_date)

# Data analysis: Total revenue for each product
total_revenue_by_product = df.groupby('Product')['TotalRevenue'].sum()
print("\nTotal revenue for each product:")
print(total_revenue_by_product)

# Data analysis: Average price and quantity sold for each product
average_price_quantity = df.groupby('Product').agg({'Price': 'mean', 'Quantity': 'mean'})
print("\nAverage price and quantity sold for each product:")
print(average_price_quantity)

# Statistical analysis: Hypothesis testing (example)
from scipy.stats import ttest_ind

product_a = df[df['Product'] == 'Product A']['Price']
product_b = df[df['Product'] == 'Product B']['Price']

t_stat, p_value = ttest_ind(product_a, product_b)
print("\nHypothesis testing results:")
print("T-statistic:", t_stat)
print("P-value:", p_value)
if p_value < 0.05:
    print("Reject null hypothesis: There is a significant difference in prices between Product A and Product B.")
else:
    print("Fail to reject null hypothesis: There is no significant difference in prices between Product A and Product B.")

# Data transformation: Convert 'Date' column to datetime object
df['Date'] = pd.to_datetime(df['Date'])

# Data aggregation: Group by month and calculate total revenue
df['Month'] = df['Date'].dt.month
total_revenue_by_month = df.groupby('Month')['TotalRevenue'].sum()
print("\nTotal revenue for each month:")
print(total_revenue_by_month)

# Data export: Export analyzed dataset to CSV file
df.to_csv('analyzed_dataset.csv', index=False)

