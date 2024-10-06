import pandas as pd
import statsmodels.api as sm
from statsmodels.stats.outliers_influence import variance_inflation_factor

# Load your dataset
df = pd.read_csv(
    r"C:\Users\Rudra\Desktop\CENSUS_PROJECT_WOMEN\white_birth\4_final_data\independent_variables123.csv"
)

X = df[
    [
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
        "total_insured",
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
]

X_with_const = sm.add_constant(X)


vif_data = pd.DataFrame()
vif_data["Feature"] = X.columns
vif_data["VIF"] = [
    variance_inflation_factor(X_with_const.values, i + 1) for i in range(X.shape[1])
]

print(vif_data)
