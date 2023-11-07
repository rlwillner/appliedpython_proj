#Emmet Shuman
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
  


