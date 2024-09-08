import pandas as pd

# Load your data from the CSV file
file_path = r'C:\Users\Rudra\Desktop\CENSUS_PROJECT_WOMEN\Final_Data.csv'
data = pd.read_csv(file_path)

# Move the 'Year' column to the first position
columns = ['Year'] + [col for col in data.columns if col != 'Year']  # Create new column order
data = data[columns]  # Reorder the columns

# Save the updated DataFrame to a new CSV file
updated_file_path = r'C:\Users\Rudra\Desktop\CENSUS_PROJECT_WOMEN\Final_census.csv'
data.to_csv(updated_file_path, index=False)

print(f"Updated data saved with 'Year' as the first column at {updated_file_path}")

# Print the first few rows to verify the changes
print(data.head())
