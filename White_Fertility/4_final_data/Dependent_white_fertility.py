import pandas as pd

# Load the dataset
df = pd.read_csv(
    r"C:\Users\Rudra\Desktop\CENSUS_PROJECT_WOMEN\data_without_year123.csv"
)

# Select only the column of interest (dependent variable)
# Replace 'white_Births_15_50' with the name of your dependent variable
dependent_variable_df = df[["white_Births_15_50"]]

# dependent_variable_df.to_csv("dependent_variable123.csv", index=False)
