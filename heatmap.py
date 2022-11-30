import pandas as pd
from datetime import date
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('mode.use_inf_as_na', True)

def get_data(url:str):
    today = date.today().strftime("%Y-%m-%d")
    df = pd.read_csv(url, engine='python')
    df = df[['location', 'date', 'total_cases', 'total_deaths']]
    df.dropna(inplace=True)
    df = df.loc[df['date'] == today, :]
    df = df.drop_duplicates(subset='location', keep="first")
    df = df.convert_dtypes()
    print(df)
    df.to_csv(r'/Users/mac/Desktop/dsci510/final/data_for_tableau.csv', index=False)


if __name__ == '__main__':
    url = "https://covid.ourworldindata.org/data/owid-covid-data.csv"
    get_data(url)

