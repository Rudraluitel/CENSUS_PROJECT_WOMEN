import pandas as pd

# Load your existing data (without 2020 data) from a CSV file
file_path = r'C:\Users\Rudra\Desktop\CENSUS_PROJECT_WOMEN\census_data_all.csv'
all_data = pd.read_csv(file_path)

# Check if 2020 data is missing
if not (all_data['Year'] == 2020).any():
    print("2020 data missing, adding manually...")

    # Manually create the missing 2020 data
    data_2020 = {
        "TB": [3982654],    # Total Births 
        "WFP": [42462812],  # White Female Population 
        "TFP": [76683447],  # Total Female Population 
        "WB": [2127510],    # White Births 
        "HFP": [15599479],  # Hispanic Female Population 
        "HB": [874874],     # Hispanic Births 
        "AFP": [5178900],   # Asian Female Population 
        "AB": [261103],     # Asian Births 
        "AAFP": [10745156], # African American Female Population 
        "AAB": [579056],    # African American Births
        "Year": [2020]      # Year
    }
    
    # Convert the dictionary to a DataFrame
    df_2020 = pd.DataFrame(data_2020)

    # Find the index of the last row for 2019
    index_2019_end = all_data[all_data['Year'] == 2019].index[-1] if not all_data[all_data['Year'] == 2019].empty else -1

    # Insert the 2020 data right after the 2019 data
    all_data = pd.concat([all_data.iloc[:index_2019_end+1], df_2020, all_data.iloc[index_2019_end+1:]], ignore_index=True)

# Save the updated DataFrame with 2020 data to a new CSV file
csv_file_path = r'C:\Users\Rudra\Desktop\CENSUS_PROJECT_WOMEN\updated_census_data_2010_2022.csv'
all_data.to_csv(csv_file_path, index=False)

print(f"Data saved to {csv_file_path}")

