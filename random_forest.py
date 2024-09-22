# Import necessary libraries
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt

# Load your dataset (replace 'your_data.csv' with the actual file path)
data = pd.read_csv(r"C:\Users\Rudra\Desktop\CENSUS_PROJECT_WOMEN\data_without_year.csv")

# Step 2: Separate independent and dependent variables
X = data.drop(columns=["white_Births_15_50"])  # Independent variables (32 in your case)
y = data["white_Births_15_50"]  # Dependent variable

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Step 1: Standardize the Data
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Step 2: Perform PCA
pca = PCA(n_components=3)  # Choose the number of components (e.g., 3 components)
X_train_pca = pca.fit_transform(X_train_scaled)
X_test_pca = pca.transform(X_test_scaled)

# Check how much variance is explained by the components
explained_variance = pca.explained_variance_ratio_
print(f"Explained Variance by each component: {explained_variance}")
print(f"Total explained variance by 3 components: {np.sum(explained_variance)}")

# Step 3: Train Random Forest on PCA-transformed data
rf = RandomForestRegressor(random_state=42)
rf.fit(X_train_pca, y_train)

# Step 4: Make predictions
y_pred = rf.predict(X_test_pca)

# Step 5: Evaluate the model
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"Mean Squared Error (MSE): {mse}")
print(f"R-squared (R²): {r2}")

# Step 6: Plot Actual vs Predicted values
plt.scatter(y_test, y_pred)
plt.xlabel("Actual White Births")
plt.ylabel("Predicted White Births")
plt.title("Actual vs Predicted White Births with PCA")
plt.show()
