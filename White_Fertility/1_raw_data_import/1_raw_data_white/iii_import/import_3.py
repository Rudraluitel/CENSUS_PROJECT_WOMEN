import requests
import pandas as pd

api_key = "98bafc056250a129981d09211487ed2349f909f5"

variables = [
    # "B27001A_009E",
    # "B27001A_012E",
    # "B27001A_015E",
    "B27003_001E",
    "B27003_039E",
    "B27003_042E",
    "B27003_045E",
    "B25014_001E",
    "B25014_005E",
    "B25014_006E",
    "B25014_007E",
    "B25014_011E",
    "B25014_012E",
    "B25014_013E",
    "C24010A_008E",
    "C24010A_009E",
    "C24010A_010E",
    "C24010A_011E",
    "C24010A_012E",
    "C24010A_013E",
]
column_name = {
    # "B27001A_009E": "White_insured_18_24",
    # "B27001A_012E": "white_insured_25_34",
    # "B27001A_015E": "white isnured_34_44",
    "B27003_001E": "total_insured",
    "B27003_039E": "femal_no_public_coverage_18_24",
    "B27003_042E": "femal_no_public_coverage_25_34",
    "B27003_045E": "femal_no_public_coverage_35_44",
    "B25014_001E": "total_occupants_per_room",
    "B25014_005E": "owner_occupied_1.01_1.50_occupants",
    "B25014_006E": "owner_occupied_1.51_2_occupants",
    "B25014_007E": "owner_occupied_2plus_occupants",
    "B25014_011E": "renter_occupied_1.01_1.50_occupants",
    "B25014_012E": "renter_occupied_1.01_1.50_occupants",
    "B25014_013E": "renter_occupied_1.01_1.50_occupants",
    "C24010A_008E": "white_female_civilian_employed",
    "C24010A_009E": "white_female_management_employed",
    "C24010A_010E": "white_female_service_employed",
    "C24010A_011E": "white_female_sales_employed",
    "C24010A_012E": "white_female_natural_resources_employed",
    "C24010A_013E": "white_female_production_employed",
}

all_years_data = []

for year in range(2012, 2023):  #  2010 to 2012(acs1) and 2013 to 2022 (acs5)
    print(f"Fetching data for year {year}...")

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
    # final_df.to_csv("c2_raw_data.csv", index=False)
else:
    print("No data fetched for any year.")

print(all_years_data.head())
