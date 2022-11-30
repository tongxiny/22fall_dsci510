# 22fall_dsci510
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
