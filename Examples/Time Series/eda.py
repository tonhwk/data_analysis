import pandas as pd
import matplotlib.pyplot as plt

# Load your time series data
df = pd.read_csv('monthly_sales.csv', parse_dates=['date'], index_col='date')

# Plot the time series
plt.figure(figsize=(12, 6))
plt.plot(df['value'])
plt.title('Time Series Plot')
plt.xlabel('Date')
plt.ylabel('Value')
plt.show()
