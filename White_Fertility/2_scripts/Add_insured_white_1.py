import pandas as pd

# Load the CSV file
file_path = r"C:\Users\Rudra\Desktop\CENSUS_PROJECT_WOMEN\white_birth\2_Scripts\med_income_updated_1.csv"
df = pd.read_csv(file_path)

new_values = {
    2012: 194497291,
    2013: 194651933,
    2014: 194662444,
}

for year, total_white_insured in new_values.items():
    df.loc[df["Year"] == year, "total_insured_white"] = total_white_insured

print(df.head())


# df.to_csv("insured_white_update2.csv", index=False)
