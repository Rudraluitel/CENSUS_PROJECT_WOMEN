import requests
import pandas as pd

api = "98bafc056250a129981d09211487ed2349f909f5"
url_acs1 = "https://api.census.gov/data/{year}/acs/acs1/subject"
url_acs5 = "https://api.census.gov/data/2020/acs/acs5/subject"

variables = [
    "S1301_C02_014E",
    "S1301_C01_001E",
    "S1301_C01_014E",
    "S1301_C02_001E",
    "S1301_C01_002E",
    "S1301_C01_003E",
    "S1301_C01_004E",
    "S1301_C01_017E",
    "S1301_C01_018E",
    "S1301_C01_019E",
    "S1301_C01_020E",
    "S1301_C01_021E",
    "S1301_C01_027E",
    "S1301_C01_029E",
    "S1301_C01_030E",
    "S1301_C01_022E",
    "S1301_C01_023E",
    "S1301_C01_025E",
    "S1201_C01_026E",
    "S1201_C02_026E",
    "S1201_C04_026E",
    "S1201_C06_026E",
    "S2701_C01_015E",
    "S1903_C02_010E",  # "S1903_C03_010E" from 2017 onwards
]

column_name = {
    "S1301_C02_014E": "white_Births_15_50",
    "S1301_C01_001E": "Female_Pop_15_50",
    "S1301_C01_014E": "white_Female_Pop_15_50",
    "S1301_C02_001E": "total_Births_15_50",
    "S1301_C01_002E": "female_Age_15_19",
    "S1301_C01_003E": "female_Age_20_34",
    "S1301_C01_004E": "female_Age_35_50",
    "S1301_C01_017E": "female_Edu_Less_HS_15_50",
    "S1301_C01_018E": "female_Edu_HS_Grad_15_50",
    "S1301_C01_019E": "female_Edu_Some_College_15_50",
    "S1301_C01_020E": "female_Edu_Bachelors_15_50",
    "S1301_C01_021E": "female_Edu_Grad_Prof_15_50",
    "S1301_C01_027E": "female_Labor_Force_15_50",
    "S1301_C01_029E": "female_Pub_Assist_Yes_15_50",
    "S1301_C01_030E": "female_Pub_Assist_No_15_50",
    "S1301_C01_022E": "female_Poverty_Determined_15_50",
    "S1301_C01_023E": "female_below_Poverty_15_50,",
    "S1301_C01_025E": "female_Above_200_Poverty_15_50",
    "S1201_C01_026E": "white_pop_15plus",
    "S1201_C02_026E": "married_white_15plus",
    "S1201_C04_026E": "divorced_white_15plus",
    "S1201_C06_026E": "nm_white_15plus",
    "S2701_C01_015E": "total_insured_white",  # S2701_C01_016E from 2012 to 2014
    "S1903_C02_010E": "med_income_white",  # "S1903_C03_010E" from 2017 onwards
}

new_data1 = pd.DataFrame()

for year in range(2010, 2023 + 1):
    print(f"Retrieving data for {year}...")

    if year == 2020:
        base_url = url_acs5
    else:
        base_url = url_acs1.format(year=year)

    params = {
        "get": ",".join(variables),
        "for": "us:1",
        "key": api,
    }

    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        data = response.json()
    else:
        print(f"Failed to retrieve data for {year}: {response.status_code}")
        continue

    column = data[0]
    new_data2 = pd.DataFrame(data[1:], columns=column)

    new_data2.rename(columns=column_name, inplace=True)
    new_data2["Year"] = year

    final_data = pd.concat([new_data1, new_data2], ignore_index=True)


# new_data1.to_csv("import_1_data.csv", index=False)
print(final_data.tail())
