import requests
import pandas as pd

api_key = "98bafc056250a129981d09211487ed2349f909f5"

variables = [
    "B25003A_003E",
    "B25003A_002E",
    "B23001_107E",
    "B23001_114E",
    "B23001_121E",
    "B23001_128E",
    "B25058_001E",
]
column_name = {
    "B25003A_003E": "renter_occupied_white",
    "B25003A_002E": "owner_occupied_white",
    "B23001_107E": "female_white_20_24_employed",
    "B23001_114E": "female_white_25_29_employed",
    "B23001_121E": "female_white_30_34_employed",
    "B23001_128E": "female_white_35_44_employed",
    "B25058_001E": "median_rent",
}
all_years_data = []

for year in range(2020, 2021):
    print(f"Fetching data for year {year}...")

    acs = "acs1" if year != 2020 else "acs5"

    url = f'https://api.census.gov/data/{year}/acs/acs5?get=NAME,{",".join(variables)}&for=us:1&key={api_key}'

    response = requests.get(url)

    print(f"Status Code: {response.status_code}")
    print(f"Response Text: {response.text[:500]}")
    if response.status_code == 200:
        try:
            data = response.json()
            df = pd.DataFrame(data[1:], columns=data[0])
            df["Year"] = year
            df.rename(columns=column_name, inplace=True)
            all_years_data.append(df)
        except ValueError:
            print(f"Could not parse the data for year {year}. Skipping this year.")
    else:
        print(f"Failed to fetch data for year {year}. Skipping this year.")

if all_years_data:
    final_df = pd.concat(all_years_data, ignore_index=True)

    print(final_df)
    # final_df.to_csv("import_2b_data.csv", index=False)
else:
    print("No data fetched for any year.")

print(all_years_data.head())
