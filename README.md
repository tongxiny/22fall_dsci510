# DSCI 510 - Final Project - Correlation between Government Policies and the Spread of COVID-19 in China

# Introduction

The project explores the relationship between government policy responses and the spread of COVID-19 cases and deaths in China by means of correlation and regression analysis. It also seeks to find out which policy contributes most to epidemic prevention. It combines government action indexes from OxCGRT and COVID-19 confirmed cases/deaths from OWID dataset to pursue such analysis and visualizes it using heatmaps and line charts.

# Dependencies

* Python 3.10
* pandas 1.5.1
* urllib3 1.26.12
* jsonschema 4.14.0
* plotly 5.11.0
* bokeh 3.0.2

# Installation

```
pip install -r requirements.txt
```

# Running the project

* github repo: https://github.com/tongxiny/22fall_dsci510
```
python analysis.py
python visualization.py
```

# Data Sources

## Overview of Raw Data

|     | Oxford COVID-19 Government Response Tracker (OxCGRT)| COVID-19 Dataset by Our World in Data|
| ------------- |---------| ---------|
| Dataset Provider | Oxford: https://github.com/OxCGRT | Our World in Data: https://github.com/owid/covid-19-data|
| Data Source| https://raw.githubusercontent.com/OxCGRT/covid-policy-tracker/master/data/OxCGRT_nat_latest.csv| https://covid.ourworldindata.org/data/owid-covid-data.csv|
| Extraction Method | pd.read_csv(url) | pd.read_csv(url)|
|Shape|(199155,61)|(238705,67)|
|Time Series|2020/01/01 till now|2020/02/24 till now|

## Data Modification

Raw data are modified according to different purposes, including correlation analysis, spacial visualization, and timeseries visualization.

### Correlation Analysis

To analyze the correlation between government policies and covid deaths/cases in China, I first filtered both datasets by location, then converted date column in both datasets to datetime format, dropped duplicates in date, inner joined two tables using location and date. Finally, I selected columns for correlation analysis in the merged dataframe and dropped rest columns. The description for modified data sample for correlation analysis is below.

<img width="2056" alt="image" src="https://user-images.githubusercontent.com/111823275/206781158-5ed588ef-9903-4f4c-8c8d-a72cc731d7c4.png">

### Spacial Visualization: Cumulative Confirmed Covid Deaths Worldwide Heatmap

To visualize the geographical distribution of cumulative covid deaths worldwide, I selected the most recent covid data from *Our World in Data* dataset (namely today's or yesterday's data), matched the up-to-date data with world.geojson by ISO-A3 format, then selected the location, total_deaths, and total_cases for display. Sample lines are shown below.

<img width="592" alt="image" src="https://user-images.githubusercontent.com/111823275/206784526-297bf762-a9ef-480c-9f7f-b8b2c95cc035.png">

### Timeseries Visualization: Interactive Line Growth Chart of Government Response Index Overworld

To display how government reponse to covid changes by time and explore shared patterns between countries, I selected country name, government response index, and date from *OxCGRT*, converted date to datetime format, reshaped the dataframe by pd.pivot, and created the dataframe for visualization which is indexed by date with country as columns and government response index as values. I chose 10 populous nations for visualization.

<img width="573" alt="image" src="https://user-images.githubusercontent.com/111823275/206787246-a5e6f986-32f8-4751-8060-74d083d45d84.png">

## Changes from Original Plan

In the original plan, I decided to analyze the whole data from 200+ countries, but later I noticed that the data from many countries are nah or flawed, which reduced the reliability of analysis.

# Methodology

> What kind of analyses or visualizations did you do? (Similar to Homework 2 Q3, but now you should answer based on your progress, rather than just your plan)  

## Correlation Analysis

### Conclusion

Total deaths and total cases have significant positive impacts on the government response level, containment and health policies, and economic support level.

### Methods
The analysis uses Pearson r to calculate linear correlation coefficients and p-values between indexes. All p<0.05 pairs are reported in the following table with the format of (coefficient, p-value). High-correlated pairs are highlighted as red cells.

### Report

<img width="526" alt="image" src="https://user-images.githubusercontent.com/111823275/206634752-c50059c2-325c-4987-8ce2-e64435fd8023.png">

# Visualization

- which visualization methods did we use
- why did we chose this particular way of visualizing data
- what insights are revealed through the means of this visualization

## Visualization 1: Cumulative Confirmed Covid Deaths Worldwide Heatmap - Generated by Plotly

<img width="1435" alt="Heatmap of Cummulative Covid Deaths Overworld" src="https://user-images.githubusercontent.com/111823275/206635045-8b5585ce-df64-4f44-8fd0-4d20b6eb63ab.png">

### Introduction

The heatmap displays cumulative covid deaths in the world, discretely colored by the number of deaths. It highlights countries significantly suffering from the epidemic and explores the geographical distribution pattern.

### Data Source

The code extracts up-to-date Covid data from Our World in Data (from 2020/02/24 till now) and then generates a heat map displaying the total confirmed deaths and cases worldwide.

### Methods

It uses Plotly to generate the heatmap. It matches the data frame with ISO-A3 geojson format to visualize the distribution of the covid deaths geographically.

## Visualization 2: Interactive Line Growth Chart of Government Response Index Overworld- Generated by bokeh

<img width="1439" alt="(interactive line chart) Government Response Index Overworld" src="https://user-images.githubusercontent.com/111823275/206635092-944daa2b-22aa-4f2e-ad79-0f9baed1e7b4.png">

### Introduction

The line chart visualizes the time series data of the Government Response Index in 10 countries from 2020/01/02 till now. It shows a shared pattern in the changing of government response between different countries in some periods. For example, from 2020/02/28 to 2020/04/09, all countries significantly strengthened epidemic prevention policies simultaneously.

### Data Source

The code extract government policy data from COVID-19 Government Response Tracker.

### Methods

It uses bokeh to generate the interactive line chart. Clicking the legend label allows hiding a specific line. It displays country, date, and government response index as the mouse hovers over the lines. 

# Future Work

> Given more time, what is the direction that you would want to take this project in?  

# Declaration
* Taiwan is not counted as part of China according to the dataset.
* You may get yesterday’s data instead of today’s due to daily updates in the dataset. This usually happens in the morning.
