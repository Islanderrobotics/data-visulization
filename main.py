import pandas as pd
import matplotlib.pyplot as plt
import math
from DataVisulization import DataVisulization
data = pd.read_csv("/Users/williammckeon/Sync/youtube videos/database/housing.csv")
print(data.columns)

DataVisulization(type_of_plot = "line",data = data, column_values_for_x = 'longitude',column_values_for_y = ['longitude', 'latitude', 'housing_median_age', 'total_rooms','total_bedrooms', 'population', 'households', 'median_income','median_house_value', 'ocean_proximity'], alpha=0.2)