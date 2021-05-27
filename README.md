# Surfs_Up
## Overview of the Statistical Analysis
Here we analyzed weather data contained in hawaii.sqlite using SQLAlchemy. This dataset includes temperature and precipitation measurements in Hawaii from 2010 to 2017 summarized in two tables: measurement including the station, date, and the recorded precipitation and temperature, along with station including geographic coordinates and elevation. In this analysis we query and summarize key differences in Hawaii weather data between the months of December and June.
## Results 
The summary statistics for temperature measurements (in °F) for the months of June and December are shown in june_temps.png and december_temps.png, respectively, and are summarized below:


<img width="246" alt="Screen Shot 2021-05-26 at 9 42 56 PM" src="https://user-images.githubusercontent.com/77812423/119752628-57dfe080-be6b-11eb-8fb7-b0d6f1f50198.png">

Key Differences:

* Higher average temperature in June than December, as expected.
* December temperature data has larger range than that of June.
* 27 °F difference between the maximum and minimum measurement in December versus 21 °F in June.
* Also reflected in the increased standard deviation for December data.
* Roughly equal interquartile ranges between June and December data.

# Summary
We see that on average the recorded temperature was higher in June than December by 3.9 °F. We also find there is a larger spread in the December data as shown by its increased standard deviation, indicating there are likley some December days with temperatures reaching those of June. This is also confirmed by the roughly equal maximum temperatures for each month. 
