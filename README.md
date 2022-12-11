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

In the original plan, I decided to analyze the merged covid and policy data covering 200+ countries, but later I noticed that only a limited number of countries had complete data. Most countries had missing values in one column or others. The scattered null values among countries reduced the reliability of analysis. Therefore I focused on analyzing China alone instead of an integrated study because I'm familiar with its background and culture, and most data are available within this country.

# Methodology

## Correlation Analysis

### Conclusion

Total deaths and total cases have significant positive impacts on the government response level, containment and health policies, and economic support level.

### Methods
The analysis uses Pearson r to calculate linear correlation coefficients and p-values between indexes. All p<0.05 pairs are reported in the following table with the format of (coefficient, p-value). High-correlated pairs are highlighted as red cells.

### Report

<img width="526" alt="image" src="https://user-images.githubusercontent.com/111823275/206634752-c50059c2-325c-4987-8ce2-e64435fd8023.png">

# Visualization

## Visualization 1: Cumulative Confirmed Covid Deaths Worldwide Heatmap - Generated by Plotly

<img width="1435" alt="Heatmap of Cummulative Covid Deaths Overworld" src="https://user-images.githubusercontent.com/111823275/206635045-8b5585ce-df64-4f44-8fd0-4d20b6eb63ab.png">

### Introduction

The heatmap displays cumulative covid deaths in the world, discretely colored by the number of deaths. It highlights countries significantly suffering from the epidemic and explores the geographical distribution pattern. It uses Plotly to generate the heatmap. It matches the data frame with ISO-A3 geojson format to visualize the distribution of the covid deaths geographically.

### Insights

The heatmap shows that although nations with fewer populations tend to have fewer cumulative covid deaths, countries with most covid deaths are not necessarily the most populous countries. For example, United States, Brazil, India, and Russia are countries with largest numbers of covid deaths, but there's no significant relation between deaths and populations among these countries. In fact, it's the differences among government policies that resulted in variation of deaths. We can see this in comparison with another visualization focusing on government response index.

## Visualization 2: Interactive Line Growth Chart of Government Response Index Overworld- Generated by bokeh

<img width="1439" alt="(interactive line chart) Government Response Index Overworld" src="https://user-images.githubusercontent.com/111823275/206635092-944daa2b-22aa-4f2e-ad79-0f9baed1e7b4.png">

### Introduction

The line chart visualizes the time series data of the Government Response Index in 10 countries from 2020/01/02 till now. It shows a shared pattern in the changing of government response between different countries in some periods. It uses bokeh to generate the interactive line chart. Clicking the legend label allows hiding a specific line. It displays country, date, and government response index as the mouse hovers over the lines. 

### Insights

Government Response Index is an aggregated number from 0 to 100 that reflects all indicators in the fields of containment and closure, economic, health system, vaccination, and miscellaneous policies. The interactive line chart shows that many countries took same level of government response to covid during certain periods despite that the spread of epidemic varied between countries at these time. For example, from 2020/02/28 to 2020/04/09, all countries significantly strengthened epidemic prevention policies simultaneously. However, at that time, covid hadn't become prevailing outside of China. This implies that other countries qucikly adopted Chinese policies at the beginning of covid. In contrast, from 2021 till now, most countries are easing their covid policy with China as the only exception. The chart vividly illustrates the adoption, easing and reimposition of covid policies among governments which is a critical pointcut for future researchers.

### Methods


# Future Work

I would like to improve the analysis part in my project given more time. I conducted a simple correlation analysis in this project. In the future,
