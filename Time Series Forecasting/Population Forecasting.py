# White Female Pop Forecast
import pandas as pd
import numpy as np
from statsmodels.tsa.arima.model import ARIMA
import matplotlib.pyplot as plt

# Load the dataset
data = pd.read_csv("C:/Users/Rudra/Desktop/CENSUS_PROJECT_WOMEN/Data_Final.csv")

# Example: Forecasting White Female Population (WFP) until 2030

# Select data for the White Female Population
white_pop = data[["Year", "WFP"]].set_index("Year")

# Fit ARIMA model (you may need to adjust order based on model diagnostics)
model_arima = ARIMA(white_pop, order=(1, 1, 1))
arima_fit = model_arima.fit()

# Forecast future population (up to 2030)
forecast_years = pd.date_range(start="2023", end="2031", freq="Y").year
forecast_pop = arima_fit.forecast(steps=len(forecast_years))

# Plot the historical data and forecast
plt.plot(white_pop, label="Historical Population")
plt.plot(forecast_years, forecast_pop, label="Forecasted Population", linestyle="--")
plt.title("White Female Population Forecast")
plt.xlabel("Year")
plt.ylabel("Population")
plt.legend()
plt.show()
