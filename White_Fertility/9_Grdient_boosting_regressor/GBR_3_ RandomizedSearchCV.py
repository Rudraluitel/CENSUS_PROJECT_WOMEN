import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, RandomizedSearchCV
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error
import matplotlib.pyplot as plt
from scipy.stats import randint, uniform

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

# Define the parameter distributions for RandomizedSearchCV
param_distributions = {
    "n_estimators": randint(50, 500),  # Number of boosting stages
    "learning_rate": uniform(0.01, 0.2),  # Step size shrinkage
    "max_depth": randint(3, 10),  # Maximum depth of individual trees
    "min_samples_split": randint(
        2, 10
    ),  # Minimum samples required to split an internal node
    "min_samples_leaf": randint(1, 10),  # Minimum samples required to be at a leaf node
}

# Initialize the Gradient Boosting Regressor
gbr = GradientBoostingRegressor(random_state=42)

# Initialize RandomizedSearchCV
random_search = RandomizedSearchCV(
    estimator=gbr,
    param_distributions=param_distributions,
    n_iter=100,  # Number of parameter settings sampled
    cv=5,  # Number of cross-validation folds
    n_jobs=-1,  # Use all available cores
    verbose=2,
    scoring="neg_mean_squared_error",  # Use negative MSE as the scoring metric
    random_state=42,
)

# Train the Gradient Boosting Regressor with RandomizedSearchCV
random_search.fit(X_train.drop(columns=["Year"]), y_train)

# Get the best parameters and best model
best_params = random_search.best_params_
best_gbr = random_search.best_estimator_

print(f"Best Parameters from RandomizedSearchCV: {best_params}")

# Predict on the test set using the best model
y_pred = best_gbr.predict(X_test.drop(columns=["Year"]))

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
y_future_pred = best_gbr.predict(future_years.drop(columns=["Year"]))

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
