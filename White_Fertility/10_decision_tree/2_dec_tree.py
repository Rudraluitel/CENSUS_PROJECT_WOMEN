import pandas as pd  # dec tree regressor, not done in classification
import numpy as np
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error
import matplotlib.pyplot as plt

# Load the data
df = pd.read_csv(
    r"C:\Users\Rudra\Desktop\CENSUS_PROJECT_WOMEN\White_Fertility\4_final_data\with_year_data.csv"
)

# Prepare the data
X = df.drop(columns=["white_Births_15_50"])
y = df["white_Births_15_50"]

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

# Set up the parameter grid for hyperparameter tuning
param_grid = {
    "max_depth": [3, 5, 10, None],  # Try different depths for the decision tree
    "min_samples_split": [
        2,
        5,
        10,
    ],  # Minimum samples required to split an internal node
    "min_samples_leaf": [1, 2, 5, 10],  # Minimum samples required to be at a leaf node
    "max_features": [
        None,
        "sqrt",
        "log2",
    ],  # Number of features to consider when looking for the best split
}

# Initialize the Decision Tree Regressor
dt_regressor = DecisionTreeRegressor(random_state=42)

# Initialize GridSearchCV with 5-fold cross-validation
grid_search = GridSearchCV(dt_regressor, param_grid, cv=5, scoring="r2", n_jobs=-1)

# Train the model using the grid search
grid_search.fit(X_train.drop(columns=["Year"]), y_train)

# Print out the best parameters
print("Best parameters found: ", grid_search.best_params_)

# Use the best model found by GridSearchCV
best_dt_regressor = grid_search.best_estimator_

# Make predictions on the test set
y_pred = best_dt_regressor.predict(X_test.drop(columns=["Year"]))

# Calculate metrics
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
mae = mean_absolute_error(y_test, y_pred)

# Output the metrics
print(f"Mean Absolute Error (MAE): {mae}")
print(f"Mean Squared Error (MSE): {mse}")
print(f"R-squared (R²): {r2}")

# Generate predictions for future years using the trained model
average_values = X.mean()

# Create a DataFrame for future years (2023-2026) with the same average feature values
future_years = pd.DataFrame(
    {
        "Year": [2023, 2024, 2025, 2026],
        **{col: [average_values[col]] * 4 for col in X.columns if col != "Year"},
    }
)

# Predict future white births
y_future_pred = best_dt_regressor.predict(future_years.drop(columns=["Year"]))

# Combine actual and predicted data
all_years = np.append(df["Year"], future_years["Year"])
all_births = np.append(y, y_future_pred)

# Plot the actual and predicted data
plt.figure(figsize=(10, 6))

plt.plot(df["Year"], y, color="green", marker="o", label="Actual Births")
plt.plot(
    all_years,
    all_births,
    color="red",
    linestyle="--",
    marker="x",
    label="Predicted Births",
)

plt.xlabel("Year")
plt.ylabel("White Births")
plt.title("Actual vs Predicted White Births (2010-2025)")
plt.legend()
plt.grid(True)

plt.show()
