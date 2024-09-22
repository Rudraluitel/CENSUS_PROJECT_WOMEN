import requests

metadata_url = "https://api.census.gov/data/{year}/acs/acs1"

available_years = []

for year in range(2001, 2024):
    url = metadata_url.format(year=year)
    response = requests.get(url)
    if response.status_code == 200:
        available_years.append(year)
    else:
        print(f"Data not available for year {year}: {response.status_code}")

print(f"Available years before 2010: {available_years}")
