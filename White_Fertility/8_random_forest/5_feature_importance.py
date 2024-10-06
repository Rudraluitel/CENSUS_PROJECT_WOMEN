import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor

df = pd.read_csv(
    r"C:\Users\Rudra\Desktop\CENSUS_PROJECT_WOMEN\White_Fertility\4_final_data\with_year_data.csv"
)

X = df.drop(columns=["white_Births_15_50"])
y = df["white_Births_15_50"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

# Initialize RandomForestRegressor without 'Year'
rf = RandomForestRegressor(n_estimators=100, random_state=42)
rf.fit(X_train.drop(columns=["Year"]), y_train)

# Feature Importance
feature_importance = rf.feature_importances_
features = X_train.drop(columns=["Year"]).columns  # Exclude 'Year'

# Create a DataFrame for better visualization
feature_importance_df = pd.DataFrame(
    {"Feature": features, "Importance": feature_importance}
).sort_values(by="Importance", ascending=False)

# Display feature importance
print(feature_importance_df)
