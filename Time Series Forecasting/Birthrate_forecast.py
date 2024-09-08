import pandas as pd
from sklearn.linear_model import LinearRegression
import numpy as np
import matplotlib.pyplot as plt

# Load the dataset
file_path = r"C:\Users\Rudra\Desktop\CENSUS_PROJECT_WOMEN\Data_Final.csv"
df = pd.read_csv(file_path)

# Prepare the data
X = df["Year"].values.reshape(-1, 1)  # Independent variable (Years)
years_future = np.array([2023, 2024, 2025, 2026, 2027]).reshape(
    -1, 1
)  # Years to forecast


# Function to forecast birth rates using Linear Regression
def forecast_birth_rates(y_values, group_name):
    model = LinearRegression()
    model.fit(X, y_values)

    # Predict future birth rates
    y_pred_future = model.predict(years_future)

    # Combine historical and forecasted data
    years_combined = np.concatenate((df["Year"].values, years_future.flatten()))
    y_combined = np.concatenate((y_values, y_pred_future))

    # Plot historical and forecasted data as a continuous line
    plt.plot(years_combined, y_combined, label=f"{group_name} Births", marker="o")

    return y_pred_future


# Forecast for each racial group
white_forecast = forecast_birth_rates(df["WB"].values, "White")
hispanic_forecast = forecast_birth_rates(df["HB"].values, "Hispanic")
asian_forecast = forecast_birth_rates(df["AB"].values, "Asian")
african_american_forecast = forecast_birth_rates(df["AAB"].values, "African American")

# Create a DataFrame for forecasted data
forecast_df = pd.DataFrame(
    {
        "Year": np.concatenate((df["Year"].values, years_future.flatten())),
        "White Births": np.concatenate((df["WB"].values, white_forecast)),
        "Hispanic Births": np.concatenate((df["HB"].values, hispanic_forecast)),
        "Asian Births": np.concatenate((df["AB"].values, asian_forecast)),
        "African American Births": np.concatenate(
            (df["AAB"].values, african_american_forecast)
        ),
    }
)

# Save the forecasted data to a CSV file
csv_output_path = (
    r"C:\Users\Rudra\Desktop\CENSUS_PROJECT_WOMEN\Birth_Rate_Forecasting.csv"
)
forecast_df.to_csv(csv_output_path, index=False)

# Show the plot
plt.title("Birth Rate Forecasting by Racial Group")
plt.xlabel("Year")
plt.ylabel("Births")
plt.legend(loc="upper left", bbox_to_anchor=(1, 1))
plt.grid(True)
plt.tight_layout(rect=[0, 0, 0.85, 1])

# Save the plot to a file
output_file_path = (
    r"C:\Users\Rudra\Desktop\CENSUS_PROJECT_WOMEN\Birth_Rate_Forecasting.png"
)
plt.savefig(output_file_path, bbox_inches="tight")

# Display the plot
plt.show()
