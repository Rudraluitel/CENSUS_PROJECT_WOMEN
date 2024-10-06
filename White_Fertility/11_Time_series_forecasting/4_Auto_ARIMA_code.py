import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
from pmdarima import auto_arima  # Import the auto_arima from pmdarima

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

# Use Auto-ARIMA to find the best (p, d, q) parameters
auto_arima_model = auto_arima(
    ts_data,
    start_p=0,
    start_q=0,
    max_p=5,
    max_q=5,  # Define the maximum p and q values
    d=None,  # Let auto_arima decide the 'd' parameter
    seasonal=False,  # Turn off seasonality since the data is not seasonal
    trace=True,  # Output the progress
    error_action="ignore",  # Ignore errors and continue
    suppress_warnings=True,
    stepwise=True,
)  # Use stepwise search to reduce computational cost

# Print the chosen ARIMA model summary
print(auto_arima_model.summary())

# Fit the best ARIMA model (p, d, q found by auto_arima)
model_fit = auto_arima_model

# Forecast future values
forecast_steps = 4  # Forecasting 4 years ahead
forecast = model_fit.predict(n_periods=forecast_steps)
forecast_index = pd.date_range(
    start=ts_data.index[-1] + pd.DateOffset(years=1), periods=forecast_steps, freq="Y"
)

# Create a DataFrame for the forecasted values
forecast_df = pd.DataFrame(forecast, index=forecast_index, columns=["Forecast"])
forecast_conf_int = model_fit.conf_int(alpha=0.05)  # Confidence intervals

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
    forecast_conf_int[:, 0],
    forecast_conf_int[:, 1],
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
plt.ylim(min(ts_data.min(), forecast_conf_int.min()) * 0.95, ts_data.max() * 1.05)

# Display the final plot
plt.tight_layout()
plt.show()

# Print the forecasted values
print("Forecasted White Births:")
print(forecast_df)
