import pandas as pd
import numpy as np
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from statsmodels.tsa.arima.model import ARIMA
import matplotlib.pyplot as plt

# Load the data
data_path = r"C:\Users\Rudra\Desktop\CENSUS_PROJECT_WOMEN\white_birth\4_final_data\with_year_data.csv"
df = pd.read_csv(data_path)

# Preview the data
print(df.head())

# Assume 'Year' and 'White_Births' are columns; split into features (X) and target (y)
X = df.drop(columns=["white_Births_15_50", "Year"])
y = df["white_Births_15_50"]  # Target variable (White Births)

# Step 1: Standardize the data
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Step 2: Apply PCA to achieve 92% variance and reduce to 3 components
pca = PCA(n_components=3)
X_pca = pca.fit_transform(X_scaled)

# Explained variance to ensure 92% target variance
explained_variance = np.cumsum(pca.explained_variance_ratio_)
print(f"Explained Variance by PCA components: {explained_variance}")

# Step 3: Train-test split for time series forecasting
# Assuming data from 2010 to 2022, let's train on 2010-2020 and test on 2021-2022
train_size = int(len(X_pca) * 0.85)  # 85% for training
X_train, X_test = X_pca[:train_size], X_pca[train_size:]
y_train, y_test = y[:train_size], y[train_size:]

# Step 4: Build ARIMA model using the PCA components
# Fit ARIMA on each principal component
model = ARIMA(y_train, order=(1, 1, 1))  # (p,d,q) order, you can tune this
arima_model = model.fit()

# Step 5: Forecast white births till the desired year
forecast_periods = len(X_test)  # Number of periods you want to predict (2021-2022)
forecast = arima_model.forecast(steps=forecast_periods)

# Step 6: Plotting the forecast vs actuals
plt.figure(figsize=(10, 6))
plt.plot(df["Year"][:train_size], y_train, label="Training Data")
plt.plot(df["Year"][train_size:], y_test, label="Actual White Births (Test)")
plt.plot(
    df["Year"][train_size:], forecast, label="Predicted White Births", linestyle="--"
)
plt.xlabel("Year")
plt.ylabel("White Births")
plt.title("White Births Prediction with Time Series Model")
plt.legend()
plt.show()

# Step 7: Evaluate the model
# You can calculate metrics like RMSE or MAE to assess the accuracy
from sklearn.metrics import mean_squared_error

rmse = np.sqrt(mean_squared_error(y_test, forecast))
print(f"Root Mean Squared Error (RMSE): {rmse}")

# Step 8: Forecast future white births (e.g., for years beyond 2022)
future_forecast_years = 5  # You can adjust this
future_forecast = arima_model.forecast(steps=future_forecast_years)
print(
    f"Future White Births Forecast for next {future_forecast_years} years: {future_forecast}"
)
