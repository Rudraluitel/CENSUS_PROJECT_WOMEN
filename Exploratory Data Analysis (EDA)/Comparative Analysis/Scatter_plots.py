# Create side-by-side visualizations (scatter plot) comparing the
# population-to-birth ratio for each race.

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
file_path = r"C:\Users\Rudra\Desktop\CENSUS_PROJECT_WOMEN\Data_Final.csv"
df = pd.read_csv(file_path)

# Calculate Population-to-Birth Ratio for each race
df["White_Ratio"] = df["WB"] / df["WFP"]
df["Hispanic_Ratio"] = df["HB"] / df["HFP"]
df["Asian_Ratio"] = df["AB"] / df["AFP"]
df["African_American_Ratio"] = df["AAB"] / df["AAFP"]
df["Other_Ratio"] = df["OTB"] / df["OTP"]
df["Total_Ratio"] = df["TB"] / df["TFP"]

# Prepare the data for visualization
ratio_df = df[
    [
        "Year",
        "White_Ratio",
        "Hispanic_Ratio",
        "Asian_Ratio",
        "African_American_Ratio",
        "Other_Ratio",
        "Total_Ratio",
    ]
]

# Melt the DataFrame to make it easier to plot with Seaborn
melted_df = pd.melt(
    ratio_df, id_vars=["Year"], var_name="Race", value_name="Population_Birth_Ratio"
)

# Create scatter plot
plt.figure(figsize=(12, 8))
sns.scatterplot(
    x="Year",
    y="Population_Birth_Ratio",
    hue="Race",
    data=melted_df,
    style="Race",
    s=100,
)

# Set labels and title
plt.title("Population-to-Birth Ratio by Race (2010-2022)", fontsize=16)
plt.xlabel("Year", fontsize=12)
plt.ylabel("Population-to-Birth Ratio", fontsize=12)
plt.legend(title="Race")

# Rotate x-axis labels for better readability
plt.xticks(rotation=45)

# Show plot
plt.tight_layout()
plt.show()
