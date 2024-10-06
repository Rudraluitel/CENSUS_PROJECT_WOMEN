import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
from statsmodels.tsa.arima.model import ARIMA

# Load data
df = pd.read_csv(
    r"C:\Users\Rudra\Desktop\CENSUS_PROJECT_WOMEN\White_Fertility\4_final_data\with_year_data.csv"
)

# Convert the Year column to datetime and set as index
df["Year"] = pd.to_datetime(df["Year"], format="%Y")
df.set_index("Year", inplace=True)

# Extract the time series data for white births
ts_data = df["white_Births_15_50"]

# Decompose the time series
decomposition = sm.tsa.seasonal_decompose(ts_data, model="additive")
fig = decomposition.plot()
plt.show()

# Fit the ARIMA model
model = ARIMA(ts_data, order=(5, 1, 0))  # Adjust the p, d, q parameters if necessary
model_fit = model.fit()

# Forecast future values
forecast_steps = 4  # Forecasting 4 years ahead
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
plt.figure(figsize=(12, 7))

# Plot historical data with markers for better visibility
plt.plot(
    ts_data, label="Historical White Births", marker="o", color="blue", linewidth=2
)

# Plot forecasted data with dashed red line and markers
plt.plot(
    forecast_df, label="Forecast", color="red", linestyle="--", marker="x", linewidth=2
)

# Add a shaded confidence interval
plt.fill_between(
    forecast_df.index,
    forecast_conf_int.iloc[:, 0],
    forecast_conf_int.iloc[:, 1],
    color="red",
    alpha=0.2,
    label="Confidence Interval",
)

# Titles and labels
plt.title("White Births Forecast (Historical + Predicted)", fontsize=16)
plt.xlabel("Year", fontsize=14)
plt.ylabel("White Births", fontsize=14)
plt.xticks(combined_data.index, combined_data.index.year, rotation=45)
# Adding grid, legend, and adjusting aesthetics
plt.grid(True, linestyle="--", alpha=0.7)
plt.legend(fontsize=12)

# Set limits for better visual alignment
plt.ylim(min(ts_data.min(), forecast_conf_int.min().min()) * 0.95, ts_data.max() * 1.05)

# Display the final plot
plt.tight_layout()
plt.show()

# Print the forecasted values
print("Forecasted White Births:")
print(forecast_df)
