#  key years with 5% changes in population growth or birth rates
# (e.g., economic recessions, COVID-19).

import pandas as pd

# Load the dataset
file_path = r"C:\Users\Rudra\Desktop\CENSUS_PROJECT_WOMEN\Data_Final.csv"
df = pd.read_csv(file_path)

# Calculate percentage changes year-on-year for population and births
df["WFP_Perc_Change"] = df["WFP"].pct_change() * 100
df["WB_Perc_Change"] = df["WB"].pct_change() * 100
df["HFP_Perc_Change"] = df["HFP"].pct_change() * 100
df["HB_Perc_Change"] = df["HB"].pct_change() * 100
df["AFP_Perc_Change"] = df["AFP"].pct_change() * 100
df["AB_Perc_Change"] = df["AB"].pct_change() * 100
df["AAFP_Perc_Change"] = df["AAFP"].pct_change() * 100
df["AAB_Perc_Change"] = df["AAB"].pct_change() * 100

# Highlight significant changes (e.g., >5% change)
significant_threshold = 5
significant_years = df[
    (df["WFP_Perc_Change"].abs() > significant_threshold)
    | (df["WB_Perc_Change"].abs() > significant_threshold)
    | (df["HFP_Perc_Change"].abs() > significant_threshold)
    | (df["HB_Perc_Change"].abs() > significant_threshold)
    | (df["AFP_Perc_Change"].abs() > significant_threshold)
    | (df["AB_Perc_Change"].abs() > significant_threshold)
    | (df["AAFP_Perc_Change"].abs() > significant_threshold)
    | (df["AAB_Perc_Change"].abs() > significant_threshold)
]

# Print significant years
print("Years with significant population or birth rate changes:")
print(
    significant_years[
        [
            "Year",
            "WFP_Perc_Change",
            "WB_Perc_Change",
            "HFP_Perc_Change",
            "HB_Perc_Change",
            "AFP_Perc_Change",
            "AB_Perc_Change",
            "AAFP_Perc_Change",
            "AAB_Perc_Change",
        ]
    ]
)

# Optional: Save the results to a CSV
output_file = r"C:\Users\Rudra\Desktop\CENSUS_PROJECT_WOMEN\Exploratory Data Analysis (EDA)\Trend Visualization\Significant_Changes.csv"
significant_years.to_csv(output_file, index=False)
