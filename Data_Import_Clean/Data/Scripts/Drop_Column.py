import pandas as pd

# Load your existing data from a CSV file
file_path = r'C:\Users\Rudra\Desktop\CENSUS_PROJECT_WOMEN\UpdatedFinal.csv'
all_data = pd.read_csv(file_path)

# Drop the 'us' column if it exists
if 'us' in all_data.columns:
    all_data = all_data.drop(columns=['us'])
    print("Column 'us' has been dropped.")
else:
    print("Column 'us' does not exist in the DataFrame.")

# Save the updated DataFrame to a new CSV file
csv_file_path = r'C:\Users\Rudra\Desktop\CENSUS_PROJECT_WOMEN\updated3.csv'
all_data.to_csv(csv_file_path, index=False)

print(f"Updated data saved to {csv_file_path}")

# Check columns to ensure 'us' is removed
print("Columns in the updated file:", all_data.columns.tolist())

