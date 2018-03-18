
# -*- coding: utf-8 -*-
"""
Linear regression plot

@author: Eran Biran
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

data = pd.read_csv('C:/Users/ERANA/Desktop/Outliers_data.csv')

Mean = data.groupby(['Month','Day'])['MeanTemp'].max()
Rain = data.groupby(['Month','Day'])['Total_Precip_mm'].max()

X = Mean.values[:,np.newaxis]
y = Rain.values

model = LinearRegression()
print(model.fit(X, y))
plt.scatter(X, y,color='r')
plt.plot(X, model.predict(X),color='k')
plt.show()