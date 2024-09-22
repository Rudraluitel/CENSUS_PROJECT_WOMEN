import pandas as pd


df1 = pd.read_csv(
    r"C:\Users\Rudra\Desktop\CENSUS_PROJECT_WOMEN\white_birth\2_Scripts\updated_import_1_data.csv"
)
df2 = pd.read_csv(
    r"C:\Users\Rudra\Desktop\CENSUS_PROJECT_WOMEN\white_birth\1_raw_data_import\1_raw_data_white\iii_import\import_3_data.csv"
)

df3 = pd.read_csv(
    r"C:\Users\Rudra\Desktop\CENSUS_PROJECT_WOMEN\white_birth\1_raw_data_import\1_raw_data_white\ii_import\import_2_data.csv"
)

df1 = df1.drop(columns=["us"])
df2 = df2.drop(columns=["us", "NAME"])
df3 = df3.drop(columns=["us", "NAME"])

merged_df = pd.merge(df1, df2, on="Year")

merged_df = pd.merge(merged_df, df3, on="Year")

# merged_df.to_csv("final_data_123.csv", index=False)


print(merged_df)
