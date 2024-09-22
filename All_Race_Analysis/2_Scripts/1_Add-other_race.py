import pandas as pd

data = pd.read_csv(
    r"C:\Users\Rudra\Desktop\CENSUS_PROJECT_WOMEN\All_Race_Analysis\1_Raw_Data\raw_data1.csv"
)


data["Other_Total_Pop"] = data["Total_Female_Pop"] - (
    data["White_Female_Pop"]
    + data["Hispanic_Female_Pop"]
    + data["Asian_Female_Pop"]
    + data["African_American_Female_Pop"]
)
data["Other_Total_Births"] = data["Total_Births"] - (
    data["White_Births"]
    + data["Hispanic_Births"]
    + data["Asian_Births"]
    + data["African_American_Births"]
)

# data.to_csv("raw_data2.csv", index=False)


print(data.columns())
