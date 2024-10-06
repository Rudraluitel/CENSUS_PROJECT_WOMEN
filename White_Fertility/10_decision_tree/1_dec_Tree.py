import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error
import matplotlib.pyplot as plt

# Load the data
df = pd.read_csv(
    r"C:\Users\Rudra\Desktop\CENSUS_PROJECT_WOMEN\White_Fertility\4_final_data\with_year_data.csv"
)

# Features (excluding the target variable)
X = df.drop(columns=["white_Births_15_50"])

# Target variable (white births)
y = df["white_Births_15_50"]

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

# Create a Decision Tree Regressor with increased depth for more flexibility
dt_regressor = DecisionTreeRegressor(max_depth=5, random_state=42)

# Fit the model (excluding 'Year' from features for training)
dt_regressor.fit(X_train.drop(columns=["Year"]), y_train)

# Predict on the test set (excluding 'Year' from the test set)
y_pred = dt_regressor.predict(X_test.drop(columns=["Year"]))

# Calculate evaluation metrics
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
mae = mean_absolute_error(y_test, y_pred)

print(f"Mean Absolute Error (MAE): {mae}")
print(f"Mean Squared Error (MSE): {mse}")
print(f"R-squared (R²): {r2}")

# Prepare for future year predictions
# Estimate a trend for the 'white_Female_Pop_15_50' column (example of dynamic data)
# You can extend this method for other features based on your data trends
pop_trend_slope = (
    X["white_Female_Pop_15_50"].iloc[-1] - X["white_Female_Pop_15_50"].iloc[0]
) / (df["Year"].iloc[-1] - df["Year"].iloc[0])

# Future population predictions using the trend slope
future_population = X["white_Female_Pop_15_50"].iloc[-1] + pop_trend_slope * np.array(
    [1, 2, 3, 4]
)

# For now, keeping other feature values as the average (you can apply trend-based changes for other features similarly)
average_values = X.mean()

# Prepare a future years DataFrame with dynamic population data
future_years = pd.DataFrame(
    {
        "Year": [2023, 2024, 2025, 2026],
        "white_Female_Pop_15_50": future_population,
        **{
            col: [average_values[col]] * 4
            for col in X.columns
            if col not in ["Year", "white_Female_Pop_15_50"]
        },
    }
)

# Predict future white births (excluding 'Year' from features)
y_future_pred = dt_regressor.predict(future_years.drop(columns=["Year"]))

# Combine actual and future predictions for visualization
all_years = np.append(df["Year"], future_years["Year"])
all_births = np.append(y, y_future_pred)

# Plot actual and predicted births
plt.figure(figsize=(10, 6))

# Plot actual births
plt.plot(df["Year"], y, color="green", marker="o", label="Actual Births")

# Plot predicted future births
plt.plot(
    all_years,
    all_births,
    color="red",
    linestyle="--",
    marker="x",
    label="Predicted Births",
)

# Adding labels, title, legend, and grid
plt.xlabel("Year")
plt.ylabel("White Births")
plt.title("Actual vs Predicted White Births (2010-2025)")
plt.legend()
plt.grid(True)

# Display the plot
plt.show()
