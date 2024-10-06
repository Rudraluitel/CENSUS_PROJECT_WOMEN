import pandas as pd

new_data = pd.read_csv(
    r"C:\Users\Rudra\Desktop\CENSUS_PROJECT_WOMEN\White_Fertility\4_final_data\final_data_123.csv"
)

new_data = new_data.drop(columns=["Year", "Unnamed: 0"])

print(new_data.head())
# new_data.to_csv("data_without_year123.csv", index=False)
