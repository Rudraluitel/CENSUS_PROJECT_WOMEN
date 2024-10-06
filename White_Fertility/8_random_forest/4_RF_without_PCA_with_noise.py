import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error
import matplotlib.pyplot as plt

# Load the data
df = pd.read_csv(
    r"C:\Users\Rudra\Desktop\CENSUS_PROJECT_WOMEN\White_Fertility\4_final_data\with_year_data.csv"
)

# Define features and target
X = df.drop(columns=["white_Births_15_50"])
y = df["white_Births_15_50"]

# Split the data into train and test sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

# Initialize and train the Random Forest Regressor
non_linear_regressor = RandomForestRegressor(n_estimators=100, random_state=42)
non_linear_regressor.fit(X_train.drop(columns=["Year"]), y_train)

# Predict on the test set
y_pred = non_linear_regressor.predict(X_test.drop(columns=["Year"]))

# Calculate metrics
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
mae = mean_absolute_error(y_test, y_pred)

print(f"Mean Absolute Error (MAE): {mae}")
print(f"Mean Squared Error (MSE): {mse}")
print(f"R-squared (R²): {r2}")

# Calculate the average values for all independent variables from 2010 to 2022
average_values = X.mean()

# Forecasting white births from 2023 to 2026 using average independent variables
future_years = pd.DataFrame(
    {
        "Year": [2023, 2024, 2025, 2026],
        # Use the average values for the other variables
        **{col: [average_values[col]] * 4 for col in X.columns if col != "Year"},
    }
)

# Drop 'Year' from future data when predicting
y_future_pred = non_linear_regressor.predict(future_years.drop(columns=["Year"]))

# Introduce random variation (e.g., 0.5% random fluctuation around the prediction)
random_noise = np.random.normal(0, 0.005, len(y_future_pred))  # 0.5% noise
y_future_pred_varied = y_future_pred * (1 + random_noise)

# Combine actual and predicted data for plotting
all_years = np.append(df["Year"], future_years["Year"])
all_births = np.append(y, y_future_pred_varied)

# Plotting the actual and predicted white births
plt.figure(figsize=(10, 6))

# Plot actual white births from 2010 to 2022
plt.plot(df["Year"], y, color="green", marker="o", label="Actual Births")

# Plot predicted white births from 2023 to 2026 with variation
plt.plot(
    all_years,
    all_births,
    color="red",
    linestyle="--",
    marker="x",
    label="Predicted Births (with variation)",
)

# Label the chart
plt.xlabel("Year")
plt.ylabel("White Births")
plt.title("Actual vs Predicted White Births (2010-2026)")
plt.legend()
plt.grid(True)

# Display the chart
plt.show()
