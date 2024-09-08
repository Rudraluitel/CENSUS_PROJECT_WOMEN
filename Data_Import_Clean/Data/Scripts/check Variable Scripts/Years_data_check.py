import requests

# Base URL for the Census API to retrieve available years for ACS 1-Year Subject Tables
metadata_url = "https://api.census.gov/data/{year}/acs/acs1/subject/variables.json"

available_years = []

# Loop to check availability for years from 2000 to 2010
for year in range(2000, 2010):
    url = metadata_url.format(year=year)
    response = requests.get(url)
    if response.status_code == 200:
        available_years.append(year)
    else:
        print(f"Data not available for year {year}: {response.status_code}")

print(f"Available years before 2010: {available_years}")

