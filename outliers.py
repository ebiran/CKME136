# -*- coding: utf-8 -*-
"""
Sorting data above 20 mm of rain

@author: Eran Biran
"""
import pandas as pd
from pylab import rcParams
rcParams['figure.figsize'] = 5,4

df = pd.read_csv('C:/Users/ERANA/Desktop/Daily_clean.csv')

#focusing on high amount of rainfall, create a new dataset with over 25mm of rain.
Total_Precip = df['Total_Precip_mm']
outliers = (Total_Precip > 20)
df[outliers].to_csv('C:/Users/ERANA/Desktop/Outliers_data.csv', index = False)