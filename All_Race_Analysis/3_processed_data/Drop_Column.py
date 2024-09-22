import pandas as pd

all_data = pd.read_csv(
    r"C:\Users\Rudra\Desktop\CENSUS_PROJECT_WOMEN\All_Race_Analysis\2_Scripts\raw_data2.csv"
)

if "us" in all_data.columns:
    all_data = all_data.drop(columns=["us"])
    print("Column 'us' has been dropped.")
else:
    print("Column 'us' does not exist in the DataFrame.")

columns = ["Year"] + [col for col in all_data.columns if col != "Year"]
all_data = all_data[columns]


# all_data.to_csv("processed_data3.csv", index=False)

print(all_data.head())
