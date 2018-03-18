# -*- coding: utf-8 -*-
"""
Data by Season

@author: Eran Biran
"""
import pandas as pd
import numpy as np
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor

datasets = [pd.read_csv('C:/Users/ERANA/Desktop/Daily_clean.csv'),
pd.read_csv('C:/Users/ERANA/Desktop/Outliers_data.csv')]

# Showing pair plotting for both datasets, per season.
for data in datasets:
    seasons = []
    for month in data['Month']:
        if month in [1, 2, 12]:
            seasons.append('Winter')
        elif month in [3, 4, 5]:
            seasons.append('Spring')
        elif month in [6, 7, 8]:
            seasons.append('Summer')
        elif month in [9, 10, 11]:
            seasons.append('Fall')
    
    reduced_data = data[['MaxTemp', 'MeanTemp', 'MinTemp','Total_Precip_mm']]
    reduced_data['season'] = seasons
    
    
    sns.set(style="ticks", color_codes=True);
    palette = sns.xkcd_palette(['dark blue', 'dark green', 'gold', 'orange'])
    sns.pairplot(reduced_data, hue = 'season', diag_kind = 'kde', palette= palette, plot_kws=dict(alpha = 0.7),diag_kws=dict(shade=True))