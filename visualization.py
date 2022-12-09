import pandas as pd
from datetime import date
from datetime import timedelta
from urllib.request import urlopen
import json
import plotly.express as px
from bokeh.plotting import figure, show
from bokeh.palettes import Turbo256
from bokeh.models import DatetimeTickFormatter
from bokeh.models import Legend
from bokeh.models.tools import HoverTool
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('mode.use_inf_as_na', True)

def get_map_data(url:str):
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

def get_line_data(url:str):
    df = pd.read_csv(url, engine='python')
    df['Date'] = pd.to_datetime(df['Date'].astype(str), format='%Y%m%d')
    df = df.loc[:,['CountryName', 'GovernmentResponseIndex_Average_ForDisplay', 'Date']]
    df = df.pivot(index='Date',columns='CountryName', values='GovernmentResponseIndex_Average_ForDisplay')
    df = df.sort_values('Date')
    df= df[['Australia','Brazil','Canada','China','India','Qatar','Russia','South Africa','United Kingdom','United States']]
    return df

def get_line_chart(df):
    fig = figure(title='Government Response Index Overworld', x_axis_label='Date',width=1200, height=800,y_axis_label='Government Response Index')
    numlines = len(df.columns)
    mypalette = Turbo256[0:256:25]
    x_list = [df.index.values]*numlines
    y_list = [df[name].values for name in df]
    label_list = df.columns.values
    for (x,y,label,color) in zip(x_list,y_list,label_list,mypalette):
        fig.line(x=x, y=y, legend_label=label,line_width=2,color=color,name=label)
    fig.xaxis.formatter = DatetimeTickFormatter(days=['%Y-%M-%D'])
    fig.legend.click_policy = 'hide'
    fig.add_layout(Legend(),'right')
    fig.add_tools(HoverTool(
    tooltips=[
        ( 'Date',   '@x{%F}'),
        ( 'GovernmentResponseIndex',  '@y{%0.2f}'),
        ('Country','$name')
    ],

    formatters={
        '@x': 'datetime',
        '@y': 'printf',
        '$name': 'printf'
    },

    mode='vline'
))
    show(fig)

if __name__ == '__main__':
    url = "https://covid.ourworldindata.org/data/owid-covid-data.csv"
    df1 = get_map_data(url)
    geo_url = "https://github.com/tongxiny/22fall_dsci510/raw/main/world.geojson"
    get_map(df1, geo_url)
    gvmt_url = "https://raw.githubusercontent.com/OxCGRT/covid-policy-tracker/master/data/OxCGRT_nat_latest.csv"
    df2 = get_line_data(gvmt_url)
    get_line_chart(df2)


