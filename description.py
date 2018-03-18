# -*- coding: utf-8 -*-
"""
Describes the dataset

@author: Eran Biran
"""
import pandas as pd

datasets = [pd.read_csv('C:/Users/ERANA/Desktop/Daily_clean.csv'),
pd.read_csv('C:/Users/ERANA/Desktop/Outliers_data.csv')]
# describe both datasets (Original + Data with over 25 mm rain.)
for data in datasets:
    shape = data.shape
    print('Data shape: \n',  shape)
    
    types = data.dtypes
    print('Data types: \n',  types)

    pd.set_option('display.width', 100)
    pd.set_option('precision', 3)
    description = data.describe()
    print('Data description: \n', description)
    
    correlations = data.corr(method='pearson')#Pearson correlation
    print('Correlations:\n ', correlations)
    
    covariance = data.cov()
    print('Covariance: \n', covariance)
    
    skew = data.skew()
    print('Data skew: \n', skew)
    print('#############################################')
          