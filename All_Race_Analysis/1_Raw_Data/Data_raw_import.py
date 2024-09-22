import requests
import pandas as pd

api = "98bafc056250a129981d09211487ed2349f909f5"
data_url = "https://api.census.gov/data/{year}/acs/acs1/subject"
for_2020 = "https://api.census.gov/data/2020/acs/acs5/subject"

variables = [
    "S1301_C01_014E",
    "S1301_C02_014E",
    "S1301_C01_013E",
    "S1301_C02_013E",
    "S1301_C01_009E",
    "S1301_C02_009E",
    "S1301_C01_007E",
    "S1301_C02_007E",
    "S1301_C01_001E",
    "S1301_C02_001E",
]

column_name = {
    "S1301_C01_001E": "Total_Female_Pop",
    "S1301_C02_001E": "Total_Births",
    "S1301_C01_014E": "White_Female_Pop",
    "S1301_C02_014E": "White_Births",
    "S1301_C01_013E": "Hispanic_Female_Pop",
    "S1301_C02_013E": "Hispanic_Births",
    "S1301_C01_009E": "Asian_Female_Pop",
    "S1301_C02_009E": "Asian_Births",
    "S1301_C01_007E": "African_American_Female_Pop",
    "S1301_C02_007E": "African_American_Births",
}

all_data = pd.DataFrame()

for year in range(2010, 2022 + 1):
    print(f"Retriving data for {year}...")

    if year == 2020:
        base_url = for_2020
    else:
        base_url = data_url.format(year=year)

    params = {
        "get": ",".join(variables),
        "for": "us:1",
        "key": api,
    }

    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        data = response.json()
    else:
        print(f"failed to retrive the data for {year}: {response.status_code}")
        continue

    column = data[0]
    df = pd.DataFrame(data[1:], columns=column)

    df.rename(columns=column_name, inplace=True)
    df["Year"] = year

    all_data = pd.concat([all_data, df], ignore_index=True)

# all_data.to_csv("raw_data1.csv", index=False)
print(all_data.values())
