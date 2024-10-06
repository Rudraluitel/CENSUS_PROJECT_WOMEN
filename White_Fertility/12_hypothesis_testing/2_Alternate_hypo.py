import pandas as pd
import numpy as np
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
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

# Print the summary of the model
print(model.summary())

# Plot the explained variance of each principal component
plt.figure(figsize=(10, 6))
plt.plot(range(1, 4), pca.explained_variance_ratio_, "bo-", markersize=10)
plt.xlabel("Principal Component")
plt.ylabel("Explained Variance Ratio")
plt.title("Explained Variance Ratio of Principal Components")
plt.grid(True)
plt.show()

# Hypothesis Testing

# Alternative Hypothesis (H₁): At least one principal component explains a significant portion of the variance.

# Checking the p-values of the principal components
# For the overall model:
p_value = model.f_pvalue

# For each principal component:
component_p_values = model.pvalues[1:]  # Exclude the constant term

print("Overall Model p-value:", p_value)
print("Principal Component p-values:", component_p_values)

# Decision making
alpha = 0.07  # Significance level (1 - 0.93)

# Overall Model Test
if p_value < alpha:
    print(
        "Accept the alternative hypothesis: The principal components collectively explain a significant portion of the variance in white births."
    )
else:
    print(
        "Fail to accept the alternative hypothesis: The principal components do not collectively explain a significant portion of the variance in white births."
    )

# Individual Principal Components Tests
for i, p_val in enumerate(component_p_values, start=1):
    if p_val < alpha:
        print(
            f"Accept the alternative hypothesis for Principal Component {i}: It significantly explains the variance in white births (p-value: {p_val})."
        )
    else:
        print(
            f"Fail to accept the alternative hypothesis for Principal Component {i}: It does not significantly explain the variance in white births (p-value: {p_val})."
        )
