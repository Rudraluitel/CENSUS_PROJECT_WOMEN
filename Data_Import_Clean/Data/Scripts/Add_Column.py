import pandas as pd

# Loading the existing data from your CSV file
file_path = r'C:\Users\Rudra\Desktop\CENSUS_PROJECT_WOMEN\updated3.csv'
all_data = pd.read_csv(file_path)

# Add 'OTP' (Others Total Population) and 'OTB' (Others Total Births) columns
# OTP = TFP - (WFP + HFP + AFP + AAFP)
# OTB = TB - (WB + HB + AB + AAB)

all_data['OTP'] = all_data['TFP'] - (all_data['WFP'] + all_data['HFP'] + all_data['AFP'] + all_data['AAFP'])
all_data['OTB'] = all_data['TB'] - (all_data['WB'] + all_data['HB'] + all_data['AB'] + all_data['AAB'])

# Save the updated DataFrame to a new CSV file
csv_file_path = r'C:\Users\Rudra\Desktop\CENSUS_PROJECT_WOMEN\Final_Data.csv'
all_data.to_csv(csv_file_path, index=False)

print(f"Updated data with OTP and OTB saved to {csv_file_path}")

# Display the first few rows of the DataFrame to verify the changes
print(all_data[['Year', 'TFP', 'TB', 'WFP', 'HFP', 'AFP', 'AAFP', 'OTP', 'OTB']].head())
