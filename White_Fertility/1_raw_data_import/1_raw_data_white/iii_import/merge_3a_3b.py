import pandas as pd

data12 = pd.read_csv(
    r"C:\Users\Rudra\Desktop\CENSUS_PROJECT_WOMEN\white_birth\1_raw_data_import\1_raw_data_white\iii_import\import_3a_data.csv"
)

data22 = pd.read_csv(
    r"C:\Users\Rudra\Desktop\CENSUS_PROJECT_WOMEN\white_birth\1_raw_data_import\1_raw_data_white\iii_import\import_3b_data.csv"
)

merged_df = pd.concat([data12, data22], ignore_index=True)

# merged_df.to_csv("import_3_data.csv", index=False)

print(merged_df)
