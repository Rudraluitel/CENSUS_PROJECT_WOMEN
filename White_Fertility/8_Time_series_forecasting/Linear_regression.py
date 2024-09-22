import pandas as pd
import numpy as np
from sklearn.decomposition import PCA
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

file_path = r"C:\Users\Rudra\Desktop\CENSUS_PROJECT_WOMEN\white_birth\4_final_data\with_year_data.csv"
df = pd.read_csv(file_path)

X = df.drop(columns=["white_Births_15_50", "Year"])

y = df["white_Births_15_50"]

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

pca = PCA(n_components=3)
X_pca = pca.fit_transform(X_scaled)

X_combined = np.column_stack((X_pca, df["Year"].values))

X_train, X_test, y_train, y_test = train_test_split(
    X_combined, y, test_size=0.3, random_state=42
)

model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"Mean Squared Error: {mse}")
print(f"R-squared: {r2}")


years_future = np.array([2023, 2024, 2025])

future_features = pd.DataFrame(
    np.zeros(
        (len(years_future), X.shape[1])
    ),  # X.shape[1] should match original features
    columns=df.drop(columns=["white_Births_15_50", "Year"]).columns,
)
future_features["Year"] = years_future

future_features_scaled = scaler.transform(future_features.drop(columns=["Year"]))

X_future_pca = pca.transform(future_features_scaled)

X_future_combined = np.column_stack((X_future_pca, years_future))

y_future_pred = model.predict(X_future_combined)

years_combined = np.concatenate((df["Year"].values, years_future))
births_combined = np.concatenate((y, y_future_pred))

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
