import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error
import matplotlib.pyplot as plt

# Load your dataset
df = pd.read_csv(
    r"C:\Users\Rudra\Desktop\CENSUS_PROJECT_WOMEN\White_Fertility\4_final_data\with_year_data.csv"
)

# Define features (X) and target (y)
X = df.drop(columns=["white_Births_15_50"])
y = df["white_Births_15_50"]

# Split the dataset into training and testing sets (70% training, 30% testing)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

# Initialize the Gradient Boosting Regressor
gbr_regressor = GradientBoostingRegressor(
    n_estimators=100,  # Number of boosting stages to be run (100 estimators)
    learning_rate=0.1,  # Step size shrinkage (can tune to lower values like 0.01)
    max_depth=3,  # Maximum depth of individual estimators (set to 3 by default)
    random_state=42,  # Set a random state for reproducibility
)

# Train the Gradient Boosting Regressor (dropping 'Year' from the features)
gbr_regressor.fit(X_train.drop(columns=["Year"]), y_train)

# Predict on the test set (excluding 'Year' from test data)
y_pred = gbr_regressor.predict(X_test.drop(columns=["Year"]))

# Evaluate the model's performance using various metrics
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
mae = mean_absolute_error(y_test, y_pred)

# Print the metrics for evaluation
print(f"Mean Absolute Error (MAE): {mae}")
print(f"Mean Squared Error (MSE): {mse}")
print(f"R-squared (R²): {r2}")

# Calculate the average values for all independent variables
average_values = X.mean()

# Forecast white births for the years 2023-2026 using average independent variables
future_years = pd.DataFrame(
    {
        "Year": [2023, 2024, 2025, 2026],
        # Use average values for all variables except 'Year'
        **{col: [average_values[col]] * 4 for col in X.columns if col != "Year"},
    }
)

# Predict future white births (excluding 'Year')
y_future_pred = gbr_regressor.predict(future_years.drop(columns=["Year"]))

# Combine actual and predicted data for plotting
all_years = np.append(df["Year"], future_years["Year"])
all_births = np.append(y, y_future_pred)

# Plot the actual and predicted white births
plt.figure(figsize=(10, 6))

# Plot actual white births (2010-2022)
plt.plot(df["Year"], y, color="green", marker="o", label="Actual Births")

# Plot predicted white births (2023-2026)
plt.plot(
    all_years,
    all_births,
    color="red",
    linestyle="--",
    marker="x",
    label="Predicted Births",
)

# Label the chart
plt.xlabel("Year")
plt.ylabel("White Births")
plt.title("Actual vs Predicted White Births (2010-2026)")
plt.legend()
plt.grid(True)

# Display the chart
plt.show()
