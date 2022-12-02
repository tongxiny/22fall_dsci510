import pandas as pd
from datetime import date
from datetime import timedelta
from urllib.request import urlopen
import json
import plotly.express as px
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('mode.use_inf_as_na', True)

def get_data(url:str):
    today = date.today().strftime("%Y-%m-%d")
    yesterday = (date.today() - timedelta(days=1)).strftime("%Y-%m-%d")
    df = pd.read_csv(url, engine='python')
    df = df[['iso_code', 'location', 'date', 'total_cases', 'total_deaths']]
    df.dropna(inplace=True)
    if df.loc[df['date'] == today, :].empty:
        df = df.loc[df['date'] == yesterday, :]
    else:
        df = df.loc[df['date'] == today, :]
    df = df.drop_duplicates(subset='location', keep="first")
    df = df.convert_dtypes()
    df = df[df['iso_code'].str.contains("OWID")==False]
    return df

def get_map(df, geo_url):
    with urlopen(geo_url) as response:
        world = json.load(response)
    df = df.rename(columns={'iso_code': 'ISO_A3'})
    df = df.sort_values('total_deaths')
    a = df.iat[0,4]
    b = df.tail().iat[0,4]
    fig = px.choropleth_mapbox(df, geojson=world, locations='ISO_A3',featureidkey="properties.ISO_A3", color='total_deaths', hover_name='total_deaths', hover_data=['location','total_deaths','total_cases'], zoom=3, mapbox_style="carto-positron", opacity=0.5, labels={'reds':'total_deaths'}, title='Cumulative Confirmed Covid Deaths Worldwide',range_color=[a,b], color_continuous_scale='RdYlGn_r')
    fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
    fig.show()

if __name__ == '__main__':
    url = "https://covid.ourworldindata.org/data/owid-covid-data.csv"
    df = get_data(url)
    geo_url = "https://github.com/tongxiny/22fall_dsci510/raw/main/world.geojson"
    get_map(df,geo_url)

