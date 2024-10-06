# population-to-birth ratio for each race.

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv(
    r"C:\Users\Rudra\Desktop\CENSUS_PROJECT_WOMEN\All_Race_Analysis\3_processed_data\processed_data3.csv"
)

df["White_Ratio"] = df["White_Births"] / df["White_Female_Pop"]
df["Hispanic_Ratio"] = df["Hispanic_Births"] / df["Hispanic_Female_Pop"]
df["Asian_Ratio"] = df["Asian_Births"] / df["Asian_Female_Pop"]
df["African_American_Ratio"] = (
    df["African_American_Births"] / df["African_American_Female_Pop"]
)
df["Other_Ratio"] = df["Other_Total_Births"] / df["Other_Total_Pop"]
df["Total_Ratio"] = df["Total_Births"] / df["Total_Female_Pop"]

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

melt_df = pd.melt(
    ratio_df, id_vars=["Year"], var_name="Race", value_name="Population_Birth_Ratio"
)

plt.figure(figsize=(12, 8))
sns.barplot(x="Year", y="Population_Birth_Ratio", hue="Race", data=melt_df)

plt.title("Population-to-Birth Ratio by Race (2010-2022)", fontsize=16)
plt.xlabel("Year", fontsize=12)
plt.ylabel("Population-to-Birth Ratio", fontsize=12)
plt.legend(title="Race", prop={"size": 7})

plt.xticks(rotation=45)

plt.tight_layout()
plt.show()
