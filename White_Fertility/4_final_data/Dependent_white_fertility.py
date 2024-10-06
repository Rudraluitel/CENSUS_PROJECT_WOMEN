import pandas as pd

# Load the dataset
df = pd.read_csv(
    r"C:\Users\Rudra\Desktop\CENSUS_PROJECT_WOMEN\White_Fertility\4_final_data\data_without_year123.csv"
)

new_data = df[["white_Births_15_50"]]

# new_data.to_csv("dependent_variable123.csv", index=False)

print(new_data.head())
