# -*- coding: utf-8 -*-
"""
Dataset cleaning

Author: Eran Biran
"""
import pandas as pd
import numpy as np

df = pd.read_csv('C:/Users/ERANA/Desktop/DAILY_MERGED.csv',dtype={'Climate_ID': str})
df = df[np.isfinite(df['Total_Precip_mm'])]
df = df[np.isfinite(df['MeanTemp'])]

df =  df[df['Total_Precip_mm']>0] # Remove days with no Rainfall

#Drop classifiers with missing and irrelevant data
df = df.drop(['Climate_ID','Date_Time','Total_Rain_mm','Data_Quality','CoolDegDays','Dir of Max Gust (10s deg)','Total_Snow_cm','SpdOfMaxGust_km_h','Max Temp Flag','Min Temp Flag','Mean Temp Flag','Heat Deg Days Flag','Cool Deg Days Flag','Total Rain Flag','Total Snow Flag','Total Precip Flag','Snow_on_Grnd_cm','Snow on Grnd Flag','Dir of Max Gust Flag','Spd of Max Gust Flag','Dir of Max Gust Flag','Spd of Max Gust Flag'], axis=1)

#Insert the mean of the cllasifier to na
df = df.fillna(df.mean())

#cretae a new dataset
df.to_csv('C:/Users/ERANA/Desktop/Daily_clean.csv', index = False)


