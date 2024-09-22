import pandas as pd

# Load the dataset
df = pd.read_csv(
    r"C:\Users\Rudra\Desktop\CENSUS_PROJECT_WOMEN\data_without_year123.csv"
)

# Drop the 'Year' and 'white_Births_15_50' columns
df_independent = df.drop(columns=["white_Births_15_50"])


# df_independent.to_csv("independent_variables123.csv", index=False)

print(df_independent.head())
