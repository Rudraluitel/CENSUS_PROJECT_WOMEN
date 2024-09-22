import pandas as pd

file = r"C:\Users\Rudra\Desktop\CENSUS_PROJECT_WOMEN\white_birth\4_final_data\data_without_year123.csv"

df = pd.read_csv(file)

print(df.describe())

# df.describe().to_csv("stats_summary.csv")
