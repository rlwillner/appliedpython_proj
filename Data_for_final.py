
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
  
city = ''
# get yearly mean for desired country
# want to get rid of years that don't have all 12 months
def yearly_mean():
    df = pd.read_csv(pathname2)
    city = input("Which city would you like to plot?: ")
    data = df[df['City'] == city]
    df2 = (df.groupby(data['dt'].str[:4].rename('year'))['AverageTemperature']
         .mean().reset_index())
    x = df2["year"]
    y = df2['AverageTemperature']
    plt.scatter(x,y)
    plt.xlabel('Date')
    plt.ylabel('Temperature')
    plt.title(f'Temperature Trends in {city}')
    plt.show()

while city != 'quit':
    yearly_mean()
