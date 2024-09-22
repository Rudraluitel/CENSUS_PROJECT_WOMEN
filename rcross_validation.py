import pandas as pd
import numpy as np
from sklearn.model_selection import cross_val_score, KFold
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.pipeline import make_pipeline
import matplotlib.pyplot as plt

# Load your dataset
data = pd.read_csv(r"C:\Users\Rudra\Desktop\CENSUS_PROJECT_WOMEN\data_without_year.csv")

# Prepare your feature matrix (X) and target variable (y)
X = data.drop(columns=["white_Births_15_50"])  # Include all features
y = data["white_Births_15_50"]  # Target variable

# Standardize the features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Apply PCA with 3 components
pca = PCA(n_components=3)
X_pca_reduced = pca.fit_transform(X_scaled)

# Define your model
model = LinearRegression()

# Perform 10-fold cross-validation
cv = KFold(n_splits=10, shuffle=True, random_state=42)
cv_scores = cross_val_score(model, X_pca_reduced, y, cv=cv, scoring="r2")

print(f"Cross-validated R-squared scores: {cv_scores}")
print(f"Mean R-squared: {cv_scores.mean()}")

# Optionally, print PCA components and explained variance
print("PCA Components:")
print(pca.components_)

print("Explained Variance Ratio:")
print(pca.explained_variance_ratio_)
