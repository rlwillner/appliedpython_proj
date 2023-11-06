#Emmet Shuman
#Final Project
#Data Visualization
#Prepping for race bar chart

import pandas as pd
import numpy as np
from matplotlib import pyplot as plt


pathname = "/Users/emmetshuman/Documents/CC Sophomore Folder/AppliedPY/Final project folder/GlobalLandTemperaturesByMajorCity.csv"

def example1plot():
  df = pd.read_csv(pathname, skiprows =1)
  print(df.columns)


example1plot()
  



