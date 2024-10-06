
# White Fertility Decline in the U.S. (2010-2022)

## Overview

This project explores the decline in the fertility rates among White women (15 to 50 yrs) in the United States, focusing on the period from 2010 to 2022. The aim is to identify the factors contributing this decline and evaluate how different demographic and socio-economic factors impact White fertility rates.<u>We also aim to forecast the White birth for next 5 years using time series model</u>. This research uses data sourced from the __American Community Survey(ACS)__ 1-year estimates.  

## Problem Statement

The U.S. has experienced a notable decline in birth rates. Although, White women represent a significant portion of the population, white women birth to population ratio is lowest compared to Asian, Hispanic or Latino and African American race. we will try to understand the factors that contribute to the reduction in fertility among this group. In this project , we focus on understanding the dynamics behind this decline and aim to answer key questions: 

     1. How does White birth ratio compare to other racial groups?
     2. What factors contribute to the decline in white fertility rates? 
     3. 
     4. 

## Data Sources
The data for this research is sourced from the American Community Survey (ACS) 1-year estimates, which provide demographic, social, and economic statistics for the U.S. population. The dataset includes detailed information on female population and births across different races, focusing on the following race groups:
    1. White alone (not Hispanic or Latino)
    2. Hispanic or Latino of origin (of any race)
    3. Asian
    4. Black or African American
    5. Other race

These four groups collectively represent over 95% of the female population. The remaining female population is categorized as "Other."

## Objectives
The key objectives of this project are:
    1. Analyze birth-to-population ratios across racial groups.
    2. Investigate the decline in fertility among White women.
    3. Identify factors that are contributing to the decreasing birth rate among White women.
    4. Using time series analysis, forceast White births for next 5 years.( 2023 to 2028)
    5.  

## Methodology

    I. Data Collection

        Source: American Community Survey (ACS) 1-year estimates.
        Period: 2010-2022.

        Variables: for race based analysis (birth to population ratio)
            A. All Variables
                1. Total_Female_Pop - Total female population (ages 15-50)
                2. Total_Births - Total births (ages 15-50)
                3. White_Female_Pop - White female population (ages 15-50)
                4. White_Births - White births (ages 15-50)
                5. Hispanic_Female_Pop - Hispanic or latino female population (ages 15-50)
                6. Hispanic_Births - Hispanic or Latino births (ages 15-50)
                7. Asian_Female_Pop - Asian female population (ages 15-50)
                8. Asian_Births -  Asian births (ages 15-50)
                9. African_American_Female_Pop - african american or Black population (ages 15-50)
                10 African_American_Births -  African American or Black births (ages 15-50)
                11.Other_Female_population - Other female population (ages 15-50)
                12.Other_Births - Other Births (ages 15-50)
        
        Variables: for White Female Fertility
            A. Demographic Variables
                1.  white_Births_15_50 - White births (ages 15-50)
                2.  Female_Pop_15_50 - Total female population (ages 15-50)
                3.	white_Female_Pop_15_50 - White female population (ages 15-50)
                4.	total_Births_15_50 - Total births (ages 15-50)
                5.	female_Age_15_19 - Female population (ages 15-19)
                6.	female_Age_20_34 - Female population (ages 20-34)
                7.	female_Age_35_50 - Female population (ages 35-50)
                8.	white_pop_15plus - White population (ages 15 and older)
                9.	married_white_15plus - Married white individuals (ages 15 and older)
                10.	divorced_white_15plus - Divorced white individuals (ages 15 and older)
                11.	nm_white_15plus - Never married white individuals (ages 15 and older)

            B. Socio-economic Variables
                1.	female_Edu_Less_HS_15_50 - Females with less than a high school education (ages 15-50)
                2.	female_Edu_HS_Grad_15_50 - Females who graduated high school (ages 15-50)
                3.	female_Edu_Some_College_15_50 - Females with some college education (ages 15-50)
                4.	female_Edu_Bachelors_15_50 - Females with a bachelor's degree (ages 15-50)
                5.	female_Edu_Grad_Prof_15_50 - Females with a graduate or professional degree (ages 15-50)
                6.	female_Labor_Force_15_50 - Females in the labor force (ages 15-50)
                7.	female_Pub_Assist_Yes_15_50 - Females receiving public assistance (ages 15-50)
                8.	female_Pub_Assist_No_15_50 - Females not receiving public assistance (ages 15-50)
                9.	female_Poverty_Determined_15_50 - Females for whom poverty status is determined (ages 15-50)
                10.	female_below_Poverty_15_50 - Females below the poverty line (ages 15-50)
                11.	female_Above_200_Poverty_15_50 - Females above 200% of the poverty line (ages 15-50)
                12.	total_insured_white - Total insured white individuals
                13.	med_income_white - Median income of white individuals
                14.	white_female_20_24_employed - Employed white females (ages 20-24)
                15.	white_female_25_29_employed - Employed white females (ages 25-29)
                16.	white_female_30_34_employed - Employed white females (ages 30-34)
                17.	white_female_35_44_employed - Employed white females (ages 35-44)
                18.	femal_no_public_coverage_18_24 - Females (ages 18-24) without public health coverage
                19.	femal_no_public_coverage_25_34 - Females (ages 25-34) without public health coverage
                20.	femal_no_public_coverage_35_44 - Females (ages 35-44) without public health coverage
                21.	white_female_civilian_employed - Employed white females in civilian occupations
                22.	white_female_management_employed - White females employed in management occupations
                23.	white_female_service_employed - White females employed in service occupations
                24.	white_female_sales_employed - White females employed in sales
                25.	white_female_natural_resources_employed - White females employed in natural resources jobs
                26.	white_female_production_employed - White females employed in production jobs

            C. Housing Variables
                1.	renter_occupied_white - White individuals in renter-occupied housing
                2.	owner_occupied_white - White individuals in owner-occupied housing
                3.	median_rent - Median rent for housing
                4.	total_occupants_per_room - Total number of occupants per room
                5.	owner_occupied_1.01_1.50_occupants - Owner-occupied units with 1.01-1.50 occupants per room
                6.	owner_occupied_1.51_2_occupants - Owner-occupied units with 1.51-2 occupants per room
                7.	owner_occupied_2plus_occupants - Owner-occupied units with more than 2 occupants per room
                8.	renter_occupied_1.01_1.50_occupants - Renter-occupied units with 1.01-1.50 occupants per room

    II. Data Analysis

        A. Race-Based Analysis: 
            The female population is segmented by race (White, Hispanic, Asian, African American, and Others).
        
        B. Population-to-Birth Ratio:
            We have calculated the ratio of total births to the total female population (ages 15-50) for each racial group and plotted it over the period from 2010 to 2022.

            The following plot shows the population-to-birth ratio for various races from 2010 to 2022:
             
             ![Birth-Population-Ratio by Race](C:\Users\Rudra\Desktop\CENSUS_PROJECT_WOMEN\All_Race_Analysis\Exploratory Data Analysis (EDA)\Comparative Analysis\Birth_population_ratio.png)
         
        C. Focus on White Fertility: 
            Among all groups, the White population shows the lowest birth ratio. This leads to further investigation into the factors that might contribute to this trend. Our research will focus on this area. 
    
    III. Factors Affecting White Female Fertility
        We will explore the following factors to assess their impact on white female fertility:
            •	Demographic factors: Age distribution, marriage rates, etc.
            •	Socio-economic factors: Education levels, income, employment, and poverty rates.
            •	Health and Insurance: Access to healthcare and insurance coverage.
            •	Housing: Rent and ownership trends.

      
## Results

Population-to-Birth Ratio by Race (2010-2022)

The above plot shows the Population-to-Birth Ratio across different races over the study period. The most significant decline is observed in the White population, whereas Hispanic and African American populations show a higher ratio throughout.
