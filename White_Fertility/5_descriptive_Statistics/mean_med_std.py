import pandas as pd

data = pd.read_csv(
    r"C:\Users\Rudra\Desktop\CENSUS_PROJECT_WOMEN\White_Fertility\4_final_data\data_without_year123.csv"
)

print(data.describe())

# data.describe().to_csv("stats_summary.csv")
