import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA
from sklearn.metrics import mean_squared_error

# Create a sample time series dataset
data = {
    'Timestamp': ['2022-01-01', '2022-01-02', '2022-01-03', '2022-01-04', '2022-01-05'],
    'Value': [100, 120, 110, 130, 125]
}

# Create a DataFrame from the data
df = pd.DataFrame(data)
df['Timestamp'] = pd.to_datetime(df['Timestamp'])
df.set_index('Timestamp', inplace=True)

# Step 2: Split the data into training and testing sets
train_size = int(len(df) * 0.8)  # 80% of the data for training
train, test = df.iloc[:train_size], df.iloc[train_size:]

# Step 3: Train the ARIMA model
model = ARIMA(train['Value'], order=(1, 1, 1))  # Example order for ARIMA model
model_fit = model.fit()

# Step 4: Evaluate the model
predictions = model_fit.forecast(steps=len(test))
mse = mean_squared_error(test['Value'], predictions)
print('Mean Squared Error:', mse)

# Step 5: Plot the original data and forecasts
plt.plot(train.index, train['Value'], label='Training Data')
plt.plot(test.index, test['Value'], label='Testing Data')
plt.plot(test.index, predictions, label='Forecast')
plt.xlabel('Timestamp')
plt.ylabel('Value')
plt.title('Time Series Forecasting with ARIMA')
plt.legend()
plt.show()
