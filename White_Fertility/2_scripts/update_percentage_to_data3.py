import pandas as pd

file_path = r"C:\Users\Rudra\Desktop\CENSUS_PROJECT_WOMEN\white_birth\2_Scripts\insured_white_update2.csv"
df = pd.read_csv(file_path)


df["married_white_15plus"] = (
    ((df["married_white_15plus"] / 100) * df["white_pop_15plus"]).round().astype(int)
)
df["divorced_white_15plus"] = (
    ((df["divorced_white_15plus"] / 100) * df["white_pop_15plus"]).round().astype(int)
)
df["nm_white_15plus"] = (
    ((df["nm_white_15plus"] / 100) * df["white_pop_15plus"]).round().astype(int)
)


print(df)

# df.to_csv("updated_import_1_data.csv", index=False)
