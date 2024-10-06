import pandas as pd
import numpy as np
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
import statsmodels.api as sm
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv(
    r"C:\Users\Rudra\Desktop\CENSUS_PROJECT_WOMEN\White_Fertility\4_final_data\with_year_data.csv"
)

# Extract the dependent variable and independent variables
X = df.drop(columns=["white_Births_15_50"])  # Drop the year and dependent variable
y = df["white_Births_15_50"]

# Standardize the data
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Apply PCA
pca = PCA(n_components=3)  # Choose 3 components
X_pca = pca.fit_transform(X_scaled)

# Prepare the data for regression
X_pca_df = pd.DataFrame(X_pca, columns=[f"PC{i+1}" for i in range(X_pca.shape[1])])
X_pca_df = sm.add_constant(X_pca_df)  # Add constant term for the intercept

# Fit the regression model
model = sm.OLS(y, X_pca_df).fit()

# Print the summary of the model (this includes T-tests for each coefficient)
print(model.summary())

# Extract t-values and p-values for each component
t_values = model.tvalues
p_values = model.pvalues

# Extract specific t-test results for PC1, PC2, PC3 (excluding the constant term)
pc_t_values = t_values[1:]  # Exclude constant term
pc_p_values = p_values[1:]  # Exclude constant term

print("\nT-values for Principal Components:", pc_t_values)
print("P-values for Principal Components:", pc_p_values)

# Set a significance level for the T-test
alpha = 0.07

# Conduct the T-tests for each principal component
for i, (t_val, p_val) in enumerate(zip(pc_t_values, pc_p_values), start=1):
    if p_val < alpha:
        print(
            f"Reject the null hypothesis for Principal Component {i}: T-test indicates it significantly explains the variance in white births (p-value: {p_val:.6f})."
        )
    else:
        print(
            f"Fail to reject the null hypothesis for Principal Component {i}: T-test indicates it does not significantly explain the variance in white births (p-value: {p_val:.6f})."
        )
