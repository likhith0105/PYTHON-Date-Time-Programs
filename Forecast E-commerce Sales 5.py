# ==============================
# E-COMMERCE SALES FORECASTING
# ==============================

# 1. Import Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from statsmodels.tsa.arima.model import ARIMA
from sklearn.metrics import mean_absolute_error

# 2. Load Dataset
data = pd.read_csv("sales.csv")

# Convert date column to datetime
data['date'] = pd.to_datetime(data['date'])

# Set index
data.set_index('date', inplace=True)

print(data.head())

# 3. Visualization
plt.figure(figsize=(10,5))
plt.plot(data['sales'], label='Sales')
plt.title("E-commerce Sales Over Time")
plt.xlabel("Date")
plt.ylabel("Sales")
plt.legend()
plt.show()

# 4. Train-Test Split
train = data[:'2023-01-12']
test = data['2023-01-13':]

# 5. Build ARIMA Model
model = ARIMA(train['sales'], order=(1,1,1))
model_fit = model.fit()

# 6. Forecast
forecast = model_fit.forecast(steps=len(test))

# 7. Evaluation
mae = mean_absolute_error(test['sales'], forecast)
print("Mean Absolute Error:", mae)

# 8. Plot Results
plt.figure(figsize=(10,5))
plt.plot(train.index, train['sales'], label='Train')
plt.plot(test.index, test['sales'], label='Actual')
plt.plot(test.index, forecast, label='Forecast', linestyle='dashed')
plt.legend()
plt.title("Sales Forecast vs Actual")
plt.show()

# 9. Future Prediction (next 5 days)
future_forecast = model_fit.forecast(steps=5)
print("\nFuture Sales Prediction:")
print(future_forecast)