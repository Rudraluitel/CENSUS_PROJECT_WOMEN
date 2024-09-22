import pandas as pd
import numpy as np
from sklearn.decomposition import PCA
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

# Load the dataset
file_path = r"C:\Users\Rudra\Desktop\CENSUS_PROJECT_WOMEN\white_birth\4_final_data\with_year_data.csv"
df = pd.read_csv(file_path)

# Define independent variables (exclude 'white_births' and 'Year')
X = df.drop(columns=["white_Births_15_50", "Year"])

# Define the target variable
y = df["white_Births_15_50"]

# Scale the independent variables
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Apply PCA to independent variables
pca = PCA(n_components=3)
X_pca = pca.fit_transform(X_scaled)

# Add 'Year' back as a feature
X_combined = np.column_stack((X_pca, df["Year"].values))

# Split the data into training and testing sets (chronologically)
train_size = int(len(df) * 0.7)
X_train, X_test = X_combined[:train_size], X_combined[train_size:]
y_train, y_test = y[:train_size], y[train_size:]

# Fit the Linear Regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Make predictions on the test set
y_pred = model.predict(X_test)

# Evaluate the model
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"Mean Squared Error: {mse}")
print(f"R-squared: {r2}")

# Forecast future years (2023)
years_future = np.array([2023])
future_features = pd.DataFrame(
    np.zeros((len(years_future), X.shape[1])),
    columns=df.drop(columns=["white_Births_15_50", "Year"]).columns,
)
future_features["Year"] = years_future

# Scale future data
future_features_scaled = scaler.transform(future_features.drop(columns=["Year"]))

# Prepare future data for PCA
X_future_pca = pca.transform(future_features_scaled)

# Combine PCA-transformed features with future years
X_future_combined = np.column_stack((X_future_pca, years_future))

# Predict births for future years
y_future_pred = model.predict(X_future_combined)

# Combine historical and forecasted data for plotting
years_combined = np.concatenate((df["Year"].values, years_future))
births_combined = np.concatenate((y, y_future_pred))

# Plot the results
plt.figure(figsize=(10, 6))
plt.plot(df["Year"], df["white_Births_15_50"], label="Actual White Births", marker="o")
plt.plot(
    years_combined,
    births_combined,
    label="Predicted White Births",
    linestyle="--",
    marker="o",
)
plt.xlabel("Year")
plt.ylabel("White Births")
plt.title("White Births Prediction")
plt.legend()
plt.grid(True)
plt.show()
