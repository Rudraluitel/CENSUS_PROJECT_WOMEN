import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
from statsmodels.tsa.arima.model import ARIMA

df = pd.read_csv(
    r"C:\Users\Rudra\Desktop\CENSUS_PROJECT_WOMEN\White_Fertility\4_final_data\with_year_data.csv"
)

df["Year"] = pd.to_datetime(df["Year"], format="%Y")
df.set_index("Year", inplace=True)

ts_data = df["white_Births_15_50"]

# Plot the historical data
plt.figure(figsize=(10, 6))
plt.plot(ts_data, label="Historical White Births")
plt.title("Historical White Births")
plt.xlabel("Year")
plt.ylabel("White Births")
plt.legend()
plt.show()

# Decompose the time series
decomposition = sm.tsa.seasonal_decompose(ts_data, model="additive")
fig = decomposition.plot()
plt.show()

# Fit the ARIMA model
# Adjust the parameters (p, d, q) as needed
model = ARIMA(ts_data, order=(5, 1, 0))  # (p, d, q) parameters
model_fit = model.fit()

# Forecast future values
forecast_steps = 4  # Number of years to forecast
forecast = model_fit.get_forecast(steps=forecast_steps)
forecast_index = pd.date_range(
    start=ts_data.index[-1] + pd.DateOffset(years=1), periods=forecast_steps, freq="Y"
)
forecast_df = pd.DataFrame(
    forecast.predicted_mean.values, index=forecast_index, columns=["Forecast"]
)
forecast_conf_int = forecast.conf_int()

# Combine actual and forecast data for plotting
combined_data = pd.concat([ts_data, forecast_df], axis=1)

# Plot the historical and forecasted data
plt.figure(figsize=(10, 6))
plt.plot(ts_data, label="Historical White Births")
plt.plot(forecast_df, label="Forecast", color="red", linestyle="--")
plt.fill_between(
    forecast_df.index,
    forecast_conf_int.iloc[:, 0],
    forecast_conf_int.iloc[:, 1],
    color="red",
    alpha=0.3,
)
plt.title("White Births Forecast")
plt.xlabel("Year")
plt.ylabel("White Births")
plt.legend()
plt.grid(True)
plt.show()

# Print the forecasted values
print("Forecasted White Births:")
print(forecast_df)
