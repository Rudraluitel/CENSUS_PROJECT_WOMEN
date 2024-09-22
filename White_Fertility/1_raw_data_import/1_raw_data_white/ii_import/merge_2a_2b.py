import pandas as pd

d1 = pd.read_csv(
    r"C:\Users\Rudra\Desktop\CENSUS_PROJECT_WOMEN\white_birth\1_raw_data_import\1_raw_data_white\ii_import\import_2a_data.csv"
)

d2 = pd.read_csv(
    r"C:\Users\Rudra\Desktop\CENSUS_PROJECT_WOMEN\white_birth\1_raw_data_import\1_raw_data_white\ii_import\import_2b_data.csv"
)

d3 = pd.concat([d1, d2], ignore_index=True)

d4 = d3.sort_values(by="Year", ascending=True)

# d4.to_csv("import_2_data.csv")
print(d4.tail())
