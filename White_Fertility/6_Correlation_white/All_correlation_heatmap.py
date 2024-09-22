import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv(
    r"C:\Users\Rudra\Desktop\CENSUS_PROJECT_WOMEN\White_Fertility\4_final_data\data_without_year123.csv"
)

columns_for_correlation = [
    "white_Births_15_50",
    "Female_Pop_15_50",
    "white_Female_Pop_15_50",
    "total_Births_15_50",
    "female_Age_15_19",
    "female_Age_20_34",
    "female_Edu_Less_HS_15_50",
    "female_Age_35_50",
    "female_Edu_HS_Grad_15_50",
    "female_Edu_Some_College_15_50",
    "female_Edu_Bachelors_15_50",
    "female_Edu_Grad_Prof_15_50",
    "female_Labor_Force_15_50",
    "female_Pub_Assist_Yes_15_50",
    "female_Pub_Assist_No_15_50",
    "female_Poverty_Determined_15_50",
    "female_below_Poverty_15_50,",
    "female_Above_200_Poverty_15_50",
    "white_pop_15plus",
    "married_white_15plus",
    "divorced_white_15plus",
    "nm_white_15plus",
    "total_insured_white",
    "med_income_white",
    "renter_occupied_white",
    "owner_occupied_white",
    "female_white_20_24_employed",
    "female_white_25_29_employed",
    "female_white_30_34_employed",
    "female_white_35_44_employed",
    "median_rent",
    "femal_no_public_coverage_18_24",
    "femal_no_public_coverage_25_34",
    "femal_no_public_coverage_35_44",
    "total_occupants_per_room",
    "owner_occupied_1.01_1.50_occupants",
    "owner_occupied_1.51_2_occupants",
    "owner_occupied_2plus_occupants",
    "renter_occupied_1.01_1.50_occupants",
    "renter_occupied_1.01_1.50_occupants",
    "renter_occupied_1.01_1.50_occupants",
    "white_female_civilian_employed",
    "white_female_management_employed",
    "white_female_service_employed",
    "white_female_sales_employed",
    "white_female_natural_resources_employed",
    "white_female_production_employed",
]

df_new = df[columns_for_correlation]


correlation = df_new.corr()


plt.figure(figsize=(14, 10))
heatmap = sns.heatmap(
    correlation,
    annot=True,
    fmt=".2f",
    cmap="coolwarm",
    linewidths=0.3,
    vmin=-1,
    vmax=1,
    cbar_kws={"shrink": 0.1},
    annot_kws={"size": 4},
)

plt.title("Correlation of White Births (15-50) with Other Variables", fontsize=16)
plt.xticks(rotation=90, fontsize=5)
plt.yticks(rotation=0, fontsize=5)

plt.tight_layout()
plt.show()

# correlation.to_csv("correlation_matrix.csv")
