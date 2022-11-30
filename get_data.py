import pandas as pd
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('mode.use_inf_as_na', True)
owid_url = "https://covid.ourworldindata.org/data/owid-covid-data.csv"
gvmt_url = "https://raw.githubusercontent.com/OxCGRT/covid-policy-tracker/master/data/OxCGRT_nat_latest.csv"


if __name__ == '__main__':
    df_gvmt = pd.read_csv(gvmt_url, engine='python')
    df_owid = pd.read_csv(owid_url, engine='python')
    df1 = df_gvmt.loc[df_gvmt['CountryName'] == 'China', :]
    df1 = df1[['CountryName', 'Date', 'StringencyIndex_Average_ForDisplay', 'GovernmentResponseIndex_Average_ForDisplay','ContainmentHealthIndex_Average_ForDisplay','EconomicSupportIndex_ForDisplay']]
    df2 = df_owid.loc[df_owid['location'] == 'China', :]
    '''df2 = df2[['location', 'date', 'total_cases', 'new_cases',
       'new_cases_smoothed', 'total_deaths', 'new_deaths',
       'new_deaths_smoothed', 'total_cases_per_million',
       'new_cases_per_million', 'new_cases_smoothed_per_million',
       'total_deaths_per_million', 'new_deaths_per_million',
       'new_deaths_smoothed_per_million', 'reproduction_rate', 'icu_patients',
       'icu_patients_per_million', 'hosp_patients',
       'hosp_patients_per_million', 'weekly_icu_admissions',
       'weekly_icu_admissions_per_million', 'weekly_hosp_admissions',
       'weekly_hosp_admissions_per_million', 'total_tests', 'new_tests',
       'total_tests_per_thousand', 'new_tests_per_thousand',
       'new_tests_smoothed', 'new_tests_smoothed_per_thousand',
       'positive_rate', 'tests_per_case', 'tests_units', 'total_vaccinations',
       'people_vaccinated', 'people_fully_vaccinated', 'total_boosters',
       'new_vaccinations', 'new_vaccinations_smoothed',
       'total_vaccinations_per_hundred', 'people_vaccinated_per_hundred',
       'people_fully_vaccinated_per_hundred', 'total_boosters_per_hundred',
       'new_vaccinations_smoothed_per_million',
       'new_people_vaccinated_smoothed',
       'new_people_vaccinated_smoothed_per_hundred', 'stringency_index',
       'gdp_per_capita', 'extreme_poverty', 'cardiovasc_death_rate','handwashing_facilities', 'hospital_beds_per_thousand',
       'life_expectancy', 'human_development_index', 'population',
       'excess_mortality_cumulative_absolute', 'excess_mortality_cumulative',
       'excess_mortality', 'excess_mortality_cumulative_per_million']]'''
    df1.dropna(inplace=True)
    df1['Date'] = pd.to_datetime(df1['Date'].astype(str), format='%Y%m%d')
    df2['date'] = pd.to_datetime(df2['date'].astype(str), format='%Y-%m-%d')
    df = pd.merge(df1, df2, how='inner', left_on=['CountryName', 'Date'], right_on=['location', 'date'])
    df = df.convert_dtypes()
    df.to_csv("hw3_sample_data.csv", index=False)
