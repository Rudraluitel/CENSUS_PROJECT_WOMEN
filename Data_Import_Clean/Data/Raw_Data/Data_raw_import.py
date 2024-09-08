import requests
import pandas as pd

# API key for the Census API
api_key = "98bafc056250a129981d09211487ed2349f909f5"

# Base URL for the Census API (note: URL structure might change slightly between years)
base_url_template = "https://api.census.gov/data/{year}/acs/acs1/subject"

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
    "S1301_C02_001E",  # Total Births (15-50)
]

# Dictionary to map variable IDs to descriptive names
column_name = {
    "S1301_C01_001E": "TFP",
    "S1301_C02_001E": "TB",
    "S1301_C01_014E": "WFP",
    "S1301_C02_014E": "WB",
    "S1301_C01_013E": "HFP",
    "S1301_C02_013E": "HB",
    "S1301_C01_009E": "AFP",
    "S1301_C02_009E": "AB",
    "S1301_C01_007E": "AAFP",
    "S1301_C02_007E": "AAB",
}

# Initialize an empty DataFrame to store all the data
all_data = pd.DataFrame()

# Loop through each year from 2010 to 2022
for year in range(2010, 2022 + 1):
    print(f"Retrieving data for {year}...")

    # Construct the API request URL for the specific year
    base_url = base_url_template.format(year=year)

    # Construct the API request parameters
    params = {
        "get": ",".join(variables),  # Join variables with a comma for the API request
        "for": "us:1",  # Request data for the entire U.S.
        "key": api_key,  # Include the API key in the request
    }

    # Make the API request
    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        data = response.json()
    else:
        print(f"Failed to retrieve data for {year}: {response.status_code}")
        continue  # Skip to the next year if there's an error

    # Convert the data into a Pandas DataFrame
    columns = data[0]  # The first row contains the column names
    df = pd.DataFrame(data[1:], columns=columns)  # Handle all rows of data

    # Rename the columns to use descriptive names
    df.rename(columns=column_name, inplace=True)

    # Add a new column for the year
    df["Year"] = year

    # Append the data to the all_data DataFrame
    all_data = pd.concat([all_data, df], ignore_index=True)

"""print(all_data[all_data["Year"] == 2020]) #Faieled to retrived data for 2020"""

# Save the combined DataFrame to a CSV file
csv_file_path = "census_data_2010_2022_race_population_births.csv"
all_data.to_csv(csv_file_path, index=False)

# Print the first few rows of the combined DataFrame to verify the data
print(all_data.head())
print(f"Data saved to {csv_file_path}")
