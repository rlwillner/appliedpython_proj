#Emmet Shuman
#Final Project
#Data Visualization
#Prepping for race bar chart

import pandas as pd
import numpy as np
from matplotlib import pyplot as plt


pathname2 = '/Users/rebecca/Documents/code/appliedpython/project/GlobalLandTemperaturesByMajorCity.csv'
pathname = "/Users/emmetshuman/Documents/CC Sophomore Folder/AppliedPY/Final project folder/GlobalLandTemperaturesByMajorCity.csv"
df = pd.read_csv(pathname)

cities = set(df.City)

print(cities)

def example1plot():
  df = pd.read_csv(pathname)
  print(df.columns)


example1plot()
  



