import pandas as pd

# Load the CSV file
file_path = r"C:\Users\Rudra\Desktop\CENSUS_PROJECT_WOMEN\white_birth\1_raw_data_import\1_raw_data_white\i_import\import_1_data.csv"
df = pd.read_csv(file_path)

new_values = {
    2017: 65845,
    2018: 67937,
    2019: 71664,
    2020: 70843,
    2021: 75412,
    2022: 80404,
}

for year, white_med_income in new_values.items():
    df.loc[df["Year"] == year, "med_income_white"] = white_med_income

print(df)


# df.to_csv("med_income_updated_1.csv", index=False)
