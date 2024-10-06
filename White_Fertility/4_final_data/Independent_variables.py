import pandas as pd

df = pd.read_csv(
    r"C:\Users\Rudra\Desktop\CENSUS_PROJECT_WOMEN\data_without_year123.csv"
)

new_data = df.drop(columns=["white_Births_15_50"])

# df_independent.to_csv("independent_variables123.csv", index=False)

print(new_data.head())
