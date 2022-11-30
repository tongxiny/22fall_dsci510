# 22fall_dsci510
## Data Collection
### Introduction
The code merges covid data from Our World in Data and government covid policy data from OxCGRT on date and location. Cleaned data of which location is China is saved for analysis. The saved csv file keeps all columns in original owid data and policy indexes in OxCGRT data.
### Technologies
* Python 3.10
* pandas 1.5.1
### Sources
* data source 1: url = "https://covid.ourworldindata.org/data/owid-covid-data.csv" 
* data source 2: url = "https://raw.githubusercontent.com/OxCGRT/covid-policy-tracker/master/data/OxCGRT_nat_latest.csv"
## Visualization 1: Total Confirmed Covid Deaths Worldwide (Tableau heatmap)
### Introduction
The code extracts up-to-date Covid data from Our World in Data, converts it into a csv file, and then uses Tableau to generate a heat map displaying the total confirmed deaths and cases in the world.
### Technologies
* Python 3.10
* pandas 1.5.1
* Tableau Desktop 2022.3.1(20223.22.1108.0821) 64-bit
### Sources
url = "https://covid.ourworldindata.org/data/owid-covid-data.csv" 
### Declaration
* Taiwan is not counted as part of China according to the dataset.
* You may get yesterday’s data instead of today’s due to daily updates in the dataset. This usually happens in the morning.
