import pandas as pd

file_path = r"C:\Users\Rudra\Desktop\CENSUS_PROJECT_WOMEN\Data_Final.csv"
df = pd.read_csv(file_path)
summary_stats = df.describe().T[["mean", "50%", "std"]]  # 50% is median
print(summary_stats)
# saving the output in csv
summary_stats.to_csv(
    r"C:\Users\Rudra\Desktop\CENSUS_PROJECT_WOMEN\Exploratory Data Analysis (EDA)\Descriptive Statistics\Summary_mean_med_std.csv"
)
