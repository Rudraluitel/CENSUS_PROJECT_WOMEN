import pandas as pd

data = pd.read_csv(
    r"C:\Users\Rudra\Desktop\CENSUS_PROJECT_WOMEN\white_birth\4_final_data\final_data_123.csv"
)
data = data.drop(columns=["Unnamed: 0"])

new_data = data.columns.tolist()

new_data.insert(0, new_data.pop(new_data.index("Year")))

df = data[new_data]

print(df.tail())

# df.to_csv("with_year_data.csv", index=False)
