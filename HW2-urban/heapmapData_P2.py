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

# https://stackoverflow.com/questions/11869910/pandas-filter-rows-of-dataframe-with-operator-chaining
# data[(data['Monthstamp'] > 9 )  & (data['Yearstamp'] == 2017)][['city', 'LAT', 'LON']].to_csv("3monthData.csv")
data[(data['Monthstamp'] == 10 )  & (data['Yearstamp'] == 2017)][['city', 'Street', 'ZIP', 'LAT', 'LON']].to_csv("OctData.csv")
data[(data['Monthstamp'] == 11 )  & (data['Yearstamp'] == 2017)][['city', 'Street', 'ZIP','LAT', 'LON']].to_csv("NovData.csv")
data[(data['Monthstamp'] == 12 )  & (data['Yearstamp'] == 2017)][['city', 'Street', 'ZIP','LAT', 'LON']].to_csv("DecData.csv")
print(data.shape)