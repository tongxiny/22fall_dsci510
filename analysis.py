import pandas as pd
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('mode.use_inf_as_na', True)
pd.set_option('use_inf_as_na', True)
pd.set_option('display.float_format', lambda x: '%.2f' % x)
owid_url = "https://covid.ourworldindata.org/data/owid-covid-data.csv"
gvmt_url = "https://raw.githubusercontent.com/OxCGRT/covid-policy-tracker/master/data/OxCGRT_nat_latest.csv"
from scipy.stats import pearsonr
import numpy as np
np.set_printoptions(suppress=True)

def corr_pval(df):
    corr_pval_df = pd.DataFrame(index=df.columns, columns=df.columns)
    for i in range(len(corr_pval_df.index)):
        for c in range(len(corr_pval_df.columns)):
            try:
                cor, p = pearsonr(df[corr_pval_df.index[i]].dropna(), df[corr_pval_df.columns[c]].dropna())
                if p < 0.05:
                    corr_pval_df.iloc[i, c] = (cor, p)
            except:
                pass
    corr_pval_df.to_csv("hw4_correlation.csv")
    return corr_pval_df


if __name__ == '__main__':
    df_gvmt = pd.read_csv(gvmt_url, engine='python')
    df_owid = pd.read_csv(owid_url, engine='python')
    df1 = df_gvmt.loc[df_gvmt['CountryName'] == 'China', :]
    df1 = df1[['CountryName', 'Date', 'StringencyIndex_Average_ForDisplay', 'GovernmentResponseIndex_Average_ForDisplay','ContainmentHealthIndex_Average_ForDisplay','EconomicSupportIndex_ForDisplay']]
    df2 = df_owid.loc[df_owid['location'] == 'China', :]
    df2 = df2[['location', 'date', 'total_cases', 'new_cases', 'total_deaths', 'new_deaths','total_boosters','new_vaccinations','total_vaccinations','positive_rate','tests_per_case','people_vaccinated','people_fully_vaccinated']]
    df1.dropna(inplace=True)
    df1['Date'] = pd.to_datetime(df1['Date'].astype(str), format='%Y%m%d')
    df2['date'] = pd.to_datetime(df2['date'].astype(str), format='%Y-%m-%d')
    df = pd.merge(df1, df2, how='inner', left_on=['CountryName', 'Date'], right_on=['location', 'date'])
    df3 = df.drop(['date', 'Date', 'CountryName', 'location'], axis=1)
    print(corr_pval(df3))
