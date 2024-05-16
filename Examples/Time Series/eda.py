import pandas as pd
import matplotlib.pyplot as plt

#Exploratory Data Analysis (EDA)
#Performing EDA on a time series involves plotting the data, checking for trends, seasonality, and anomalies.

# Load your time series data
df = pd.read_csv('monthly_sales.csv', parse_dates=['date'], index_col='date')

# Plot the time series
plt.figure(figsize=(12, 6))
plt.plot(df['value'])
plt.title('Time Series Plot')
plt.xlabel('Date')
plt.ylabel('Value')
plt.show()
