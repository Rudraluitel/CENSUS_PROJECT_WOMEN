import pandas as pd

# Load your data from the CSV file
file_path = r"C:\Users\Rudra\Desktop\CENSUS_PROJECT_WOMEN\Final_Data.csv"
data = pd.read_csv(file_path)

# Specify the new column order, moving 'TFP' and 'TB' to the end
columns = [
    "Year",
    "WFP",
    "WB",
    "HFP",
    "HB",
    "AFP",
    "AB",
    "AAFP",
    "AAB",
    "OTP",
    "OTB",
    "TB",
    "TFP",
]
data = data[columns]  # Reorder the columns

# Save the updated DataFrame to a new CSV file
updated_file_path = r"C:\Users\Rudra\Desktop\CENSUS_PROJECT_WOMEN\Data_Final.csv"
data.to_csv(updated_file_path, index=False)

print(f"Updated data saved with 'TB' and 'TFP' at the end at {updated_file_path}")

# Print the first few rows to verify the changes
print(data.head())
