import requests
import pandas as pd

# API key for the Census API
api_key = "98bafc056250a129981d09211487ed2349f909f5"

# Base URL for the Census API
base_url = "https://api.census.gov/data/2010/acs/acs1/subject"

# List of variables to retrieve
variables = [
    "S1301_C01_014E",  # White Female Population
    "S1301_C02_014E",  # White Births
    "S1301_C01_013E",  # Hispanic Female Population
    "S1301_C02_013E",  # Hispanic Births
    "S1301_C01_009E",  # Asian Female Population
    "S1301_C02_009E",  # Asian Births
    "S1301_C01_007E",  # African American Female Population	   
    "S1301_C02_007E",  # African American Births
    "S1301_C01_001E",  # Total Female Population (15-50)
    "S1301_C02_001E"   # Total Births (15-50)
]

# Dictionary to map variable IDs to descriptive names
column_name = {
    "S1301_C01_001E": "TFP ",
    "S1301_C02_001E": "TB ",
    "S1301_C01_014E": "WFP",
    "S1301_C02_014E": "WB",
    "S1301_C01_013E": "HFP",
    "S1301_C02_013E": "HB",
    "S1301_C01_009E": "AFP",
    "S1301_C02_009E": "AB",
    "S1301_C01_007E": "AAFP",
    "S1301_C02_007E": "AAB"  
}

# Construct the API request parameters
params = {
    "get": ",".join(variables),  # Join variables with a comma for the API request
    "for": "us:1",  # Request data for the entire U.S.
    "key": api_key  # Include the API key in the request
}

# Make the API request
response = requests.get(base_url, params=params)
if response.status_code == 200:
    data = response.json()
else:
    print(f"Failed to retrieve data: {response.status_code}")
    data = None

if data:
    # Convert the data into a Pandas DataFrame
    columns = data[0]  # The first row contains the column names
    df = pd.DataFrame(data[1:], columns=columns)  # Handle all rows of data
    
    # Rename the columns to use descriptive names
    df.rename(columns=column_name, inplace=True)
    
    # Save the DataFrame to a CSV file
    csv_file_path = "census_data_2010_race_population_births.csv"
    df.to_csv(csv_file_path, index=False)
    
    # Print the first few rows of the DataFrame to verify the data
    print(df.head())
    print(f"Data saved to {csv_file_path}")
