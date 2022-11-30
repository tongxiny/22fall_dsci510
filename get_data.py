import requests
from bs4 import BeautifulSoup
import pandas as pd
import re
from scipy.stats import pearsonr
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('mode.use_inf_as_na', True)
owid_url = "https://covid.ourworldindata.org/data/owid-covid-data.csv"
gvmt_url = "https://raw.githubusercontent.com/OxCGRT/covid-policy-tracker/master/data/OxCGRT_nat_differentiated_withnotes_2022.csv"


if __name__ == '__main__':
    df_gvmt = pd.read_csv(gvmt_url, engine='python')
    df_owid = pd.read_csv(owid_url, engine='python')
    df1 = df_gvmt[['CountryName', 'Date', 'StringencyIndex_WeightedAverage_ForDisplay', 'GovernmentResponseIndex_WeightedAverage_ForDisplay','ContainmentHealthIndex_WeightedAverage_ForDisplay','EconomicSupportIndex_ForDisplay']]
    df2 = df_owid[['location', 'date', 'total_cases', 'new_cases', 'total_deaths', 'new_deaths','total_tests', 'new_tests']]
    df1['Date'] = pd.to_datetime(df1['Date'].astype(str), format='%Y%m%d')
    df2['date'] = pd.to_datetime(df2['date'].astype(str), format='%Y-%m-%d')
    df = pd.merge(df1, df2, how='inner', left_on=['CountryName', 'Date'], right_on=['location', 'date'])
    df.dropna(inplace=True)
    df = df.convert_dtypes()
    print(pearsonr(df['StringencyIndex_WeightedAverage_ForDisplay'],df['new_deaths']))

