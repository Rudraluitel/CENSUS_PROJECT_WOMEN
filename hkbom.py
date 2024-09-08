import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report

# Example data
data = {
    "White_Pop": [0.50, 0.60, 0.45, 0.55, 0.50],
    "Hispanic_Pop": [0.20, 0.25, 0.30, 0.15, 0.20],
    "Asian_Pop": [0.10, 0.05, 0.15, 0.10, 0.10],
    "African_American_Pop": [0.20, 0.10, 0.10, 0.20, 0.20],
    "High_Birth_Rate": [0, 1, 1, 0, 0],
}
df = pd.DataFrame(data)

# Features and target variable
X = df[["White_Pop", "Hispanic_Pop", "Asian_Pop", "African_American_Pop"]]
y = df["High_Birth_Rate"]

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

print("Script started")
# Your code here
print("Script ended")
