
#Final Project
#Data Visualization
#Prepping for race bar chart

import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import bar_chart_race as bcr


pathname2 = '/Users/rebecca/Documents/code/appliedpython/project/GlobalLandTemperaturesByMajorCity.csv'
pathname = "/Users/emmetshuman/Documents/CC Sophomore Folder/AppliedPY/Final project folder/GlobalLandTemperaturesByMajorCity.csv"
df = pd.read_csv(pathname)

cities = set(df.City)

print(cities)

#Okay here is a basic graph for whichever city we are interested in
#Doesn't check city for bad inputs but it does make a little graph
#Could benefit from the seasons being averaged.
#We could do like 2023 winter and 2023 summer
def Emmet():
    df = pd.read_csv(pathname)
    cities = set(df.City)

    city = input("Which city would you like to plot?: ")
    data = df[df['City'] == city]
    x = data["dt"]
    y = data["AverageTemperature"]

    plt.scatter(x, y) 
    plt.xlabel('Date')
    plt.ylabel('Temperature')
    plt.title(f'Temperature Trends in {city}')
    plt.show()

Emmet()
  
def is_nan(data):
    nan_years = []
    print(len(data))
    data_array = data["AverageTemperature"].values
    dt_array  = data["dt"].values
    print(data_array.shape)
    for i in range(len(data)):
        if math.isnan(data_array[i]):
            nan_years.append(int(dt_array[i][:4]))
    nan_years = list(set(nan_years))
    return nan_years




def yearly_mean():
    df = pd.read_csv(pathname2)
    city = input("Which city would you like to plot?: ")
    data = df[df['City'] == city].reset_index()

    df2 = (data.groupby(data['dt'].str[:4].rename('year'))['AverageTemperature']
         .mean().reset_index())
    df2.year = pd.to_numeric(df2.year)
    df3 = df2.dropna().reset_index(drop=True)
    
    nan_years = is_nan(data)
    print(type(nan_years[0]))
    print(type(df3.year.values[0]))

    df3 = df3[~df3.year.isin(nan_years)]
    print(df3)

    x = df3["year"]

    y = df3['AverageTemperature']
    plt.scatter(x,y)
    plt.xlabel('Date')
    plt.ylabel('Temperature')
    plt.title(f'Temperature Trends in {city}')
    plt.show()



while city != 'quit':
    yearly_mean()
