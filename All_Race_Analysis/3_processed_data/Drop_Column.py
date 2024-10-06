import pandas as pd

new_data1 = pd.read_csv(
    r"C:\Users\Rudra\Desktop\CENSUS_PROJECT_WOMEN\All_Race_Analysis\2_Scripts\raw_data2.csv"
)

if "us" in new_data1.columns:
    new_data1 = new_data1.drop(columns=["us"])
    print("Column 'us' has been dropped.")
else:
    print("Column 'us' does not exist in the DataFrame.")

columns = ["Year"] + [col for col in new_data1.columns if col != "Year"]
new_data1 = new_data1[columns]

# new_data1.to_csv("processed_data3.csv", index=False)

print(new_data1.head())
