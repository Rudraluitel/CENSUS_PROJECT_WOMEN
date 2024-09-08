# Use correlation heatmaps to explore relationships between the different racial
# groups and variables
# (e.g., total female population vs. total births)

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
file_path = r"C:\Users\Rudra\Desktop\CENSUS_PROJECT_WOMEN\Data_Final.csv"
df = pd.read_csv(file_path)

# Select relevant columns for correlation
columns_of_interest = [
    "WFP",
    "WB",
    "HFP",
    "HB",
    "AFP",
    "AB",
    "AAFP",
    "AAB",
    "TFP",
    "TB",
]
df_selected = df[columns_of_interest]

# Calculate correlation matrix
correlation_matrix = df_selected.corr()

# Plot the heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", linewidths=0.5)
plt.title("Correlation Heatmap of Female Population and Births by Race")
plt.show()

# correlation_matrix.to_csv(
# r"C:\Users\Rudra\Desktop\CENSUS_PROJECT_WOMEN\correlation_matrix.csv"
