import pandas as pd
import numpy as np
from sklearn.decomposition import PCA
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt

# Load your dataset
# Assuming the dataset is in a CSV file, replace with your actual path
df = pd.read_csv(r"C:\Users\Rudra\Desktop\CENSUS_PROJECT_WOMEN\data_without_year.csv")

# Step 2: Separate independent and dependent variables
X = df.drop(columns=["white_Births_15_50"])  # Independent variables (32 in your case)
y = df["white_Births_15_50"]  # Dependent variable

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Apply PCA
n_components = 3  # You can experiment with different numbers of components
pca = PCA(n_components=n_components)
X_train_pca = pca.fit_transform(X_train)
X_test_pca = pca.transform(X_test)

# Explained variance
explained_variance = pca.explained_variance_ratio_
print(f"Explained Variance by each component: {explained_variance}")
print(
    f"Total explained variance by {n_components} components: {sum(explained_variance)}"
)

# Random Forest Regressor with Hyperparameter Tuning
param_grid = {
    "n_estimators": [100, 200, 300],
    "max_depth": [None, 10, 20, 30],
    "min_samples_split": [2, 5, 10],
    "min_samples_leaf": [1, 2, 4],
}

# Initialize the Random Forest model
rf = RandomForestRegressor(random_state=42)

# Perform GridSearchCV to find the best parameters
grid_search = GridSearchCV(
    estimator=rf, param_grid=param_grid, cv=5, scoring="r2", verbose=2, n_jobs=-1
)
grid_search.fit(X_train_pca, y_train)

# Get the best model
rf_best = grid_search.best_estimator_
print(f"Best hyperparameters: {grid_search.best_params_}")

# Predict on the test set
y_pred = rf_best.predict(X_test_pca)

# Evaluate the model
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"Mean Squared Error (MSE): {mse}")
print(f"R-squared (R²): {r2}")

# Plot Actual vs Predicted values
plt.scatter(y_test, y_pred)
plt.xlabel("Actual White Births")
plt.ylabel("Predicted White Births")
plt.title("Actual vs Predicted White Births")
plt.show()
