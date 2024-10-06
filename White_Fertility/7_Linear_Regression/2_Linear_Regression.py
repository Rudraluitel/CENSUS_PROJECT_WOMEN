import pandas as pd
from sklearn.decomposition import PCA
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv(
    r"C:\Users\Rudra\Desktop\CENSUS_PROJECT_WOMEN\White_Fertility\4_final_data\with_year_data.csv"
)

X = df.drop(columns=["white_Births_15_50", "Year"])
y = df["white_Births_15_50"]
years = df["Year"]

pca = PCA(n_components=3)
X_pca = pca.fit_transform(X)

X_train, X_test, y_train, y_test, years_train, years_test = train_test_split(
    X_pca, y, years, test_size=0.3, random_state=42
)

regressor = LinearRegression()
regressor.fit(X_train, y_train)

y_pred = regressor.predict(X_test)

sorted_indices = np.argsort(years_test)
years_test_sorted = years_test.iloc[sorted_indices]
y_test_sorted = y_test.iloc[sorted_indices]
y_pred_sorted = y_pred[sorted_indices]

mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
mae = mean_absolute_error(y_test, y_pred)

print(f"Mean Absolute Error (MAE): {mae}")
print(f"Mean Squared Error (MSE): {mse}")
print(f"R-squared (R²): {r2}")

plt.figure(figsize=(12, 6))

plt.plot(
    years_test_sorted,
    y_test_sorted,
    label="Actual White Births",
    color="green",
    marker="o",
)

plt.plot(
    years_test_sorted,
    y_pred_sorted,
    label="Predicted White Births",
    color="red",
    marker="x",
)

plt.xlabel("Year")
plt.ylabel("White Births")
plt.title("Actual vs Predicted White Births Over Time")
plt.legend()

# plt.savefig("white_births_prediction_model.png", dpi=300)

plt.show()
