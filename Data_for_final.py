
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

def make_data():
    df = pd.read_csv(pathname2)

    
    city1 = input("Which city would you like to plot?: ")
    data_city1 = df[df['City'] == city1].reset_index()
    data_city1 = (data_city1.groupby(data_city1['dt'].str[:4].rename('year'))['AverageTemperature']
         .mean().reset_index())
    data_city1.year = pd.to_numeric(data_city1.year)
    data_city1.rename(columns={'AverageTemperature': city1}, inplace=True)
    data_city1 = data_city1.set_index(['year'])
    
    city2 = input("Which city would you like to plot?: ")
    data_city2 = df[df['City'] == city2].reset_index()
    data_city2 = (data_city2.groupby(data_city2['dt'].str[:4].rename('year'))['AverageTemperature']
         .mean().reset_index())
    data_city2.year = pd.to_numeric(data_city2.year)
    data_city2.rename(columns={'AverageTemperature': city2}, inplace=True)
    data_city2 = data_city2.set_index(['year'])

    city3 = input("Which city would you like to plot?: ")
    data_city3 = df[df['City'] == city3].reset_index()
    data_city3 = (data_city3.groupby(data_city3['dt'].str[:4].rename('year'))['AverageTemperature']
         .mean().reset_index())
    data_city3.year = pd.to_numeric(data_city3.year)
    data_city3.rename(columns={'AverageTemperature': city3}, inplace=True)
    data_city3 = data_city3.set_index(['year'])
    
    city4 = input("Which city would you like to plot?: ")
    data_city4 = df[df['City'] == city4].reset_index()
    data_city4 = (data_city4.groupby(data_city4['dt'].str[:4].rename('year'))['AverageTemperature']
         .mean().reset_index())
    data_city4.year = pd.to_numeric(data_city4.year)
    data_city4.rename(columns={'AverageTemperature': city4}, inplace=True)
    data_city4 = data_city4.set_index(['year'])

    city5 = input("Which city would you like to plot?: ")
    data_city5 = df[df['City'] == city5].reset_index()
    data_city5 = (data_city5.groupby(data_city5['dt'].str[:4].rename('year'))['AverageTemperature']
         .mean().reset_index())
    data_city5.year = pd.to_numeric(data_city5.year)
    data_city5.rename(columns={'AverageTemperature': city5}, inplace=True)
    data_city5 = data_city5.set_index(['year'])
    
    city6 = input("Which city would you like to plot?: ")
    data_city6 = df[df['City'] == city6].reset_index()
    data_city6 = (data_city6.groupby(data_city6['dt'].str[:4].rename('year'))['AverageTemperature']
         .mean().reset_index())
    data_city6.year = pd.to_numeric(data_city6.year)
    data_city6.rename(columns={'AverageTemperature': city6}, inplace=True)
    data_city6 = data_city6.set_index(['year'])

    city7 = input("Which city would you like to plot?: ")
    data_city7 = df[df['City'] == city7].reset_index()
    data_city7 = (data_city1.groupby(data_city7['dt'].str[:4].rename('year'))['AverageTemperature']
         .mean().reset_index())
    data_city7.year = pd.to_numeric(data_city7.year)
    data_city7.rename(columns={'AverageTemperature': city7}, inplace=True)
    data_city7 = data_city7.set_index(['year'])
    
    city8 = input("Which city would you like to plot?: ")
    data_city8 = df[df['City'] == city8].reset_index()
    data_city8 = (data_city8.groupby(data_city8['dt'].str[:4].rename('year'))['AverageTemperature']
         .mean().reset_index())
    data_city8.year = pd.to_numeric(data_city8.year)
    data_city8.rename(columns={'AverageTemperature': city8}, inplace=True)
    data_city8 = data_city8.set_index(['year'])

    city9 = input("Which city would you like to plot?: ")
    data_city9 = df[df['City'] == city9].reset_index()
    data_city9 = (data_city9.groupby(data_city9['dt'].str[:4].rename('year'))['AverageTemperature']
         .mean().reset_index())
    data_city9.year = pd.to_numeric(data_city9.year)
    data_city9.rename(columns={'AverageTemperature': city9}, inplace=True)
    data_city9 = data_city9.set_index(['year'])
    
    city10 = input("Which city would you like to plot?: ")
    data_city10 = df[df['City'] == city10].reset_index()
    data_city10 = (data_city10.groupby(data_city10['dt'].str[:4].rename('year'))['AverageTemperature']
         .mean().reset_index())
    data_city10.year = pd.to_numeric(data_city10.year)
    data_city10.rename(columns={'AverageTemperature': city10}, inplace=True)
    data_city10 = data_city10.set_index(['year'])

    all = pd.concat([data_city1, data_city2, data_city3, data_city4, data_city5, data_city6, data_city7, data_city8, data_city9, data_city10], axis=1)
    print(all)
    
make_data()
