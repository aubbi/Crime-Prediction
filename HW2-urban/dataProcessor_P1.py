import csv
import pandas as pd
import random
import numpy as np
import ephem
import math
import datetime
import matplotlib.pyplot as plt

# https://www.shanelynn.ie/select-pandas-dataframe-rows-and-columns-using-iloc-loc-and-ix/
data = pd.read_csv("Santa_Rosa_Police_Department_Calls_For_Service.csv")
data = data.iloc[1:]
print(data.shape)

# Create a dataset with the following attributes: Incident ID, Date, Longitude, Latitude.
# https://pandas.pydata.org/pandas-docs/stable/generated/pandas.to_datetime.html
dSample = data.filter(items = ['Event_Num', 'Date', 'LAT', 'LON'])
dSample.to_csv("light_crime_data.csv")

dSample['Date']=pd.to_datetime(dSample['Date'],  yearfirst=True)
dSample.index=dSample['Date']

# Separate the dataset by month.
# https://www.tutorialspoint.com/python_pandas/python_pandas_groupby.htm


grouped = dSample.groupby(by=[dSample.index.year, dSample.index.month])
for name, group in grouped:
	print(group.head())
	# https://stackoverflow.com/questions/20845213/how-to-avoid-python-pandas-creating-an-index-in-a-saved-csv
	group.to_csv("month_crime_data_" + str(name[0]) + "_" + str(name[1]) + ".csv", index = False)




dSample['Date'].groupby(by=[dSample.index.year, dSample.index.month]).agg({'count'}).to_csv("months.csv")
date = []
months = pd.read_csv("months.csv")
year = months['Date']
month = months['Date.1']
for idx, row in months.iterrows():
	date.append(str(year[idx]) + "-" + str(month[idx]))
months = months.assign(date = date)
months.filter(items = ['date', 'count']).to_csv("monthSeries.csv")
# dSample['Date'].groupby(by=[dSample.index.month]).agg({'count'}).to_csv("monthSeries_2.csv")
# print(dSample)

