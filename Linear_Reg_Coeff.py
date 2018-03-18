# -*- coding: utf-8 -*-
"""
Linear Regression Model

@author: Eran Biran
"""
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import math

df= pd.read_csv('C:/Users/ERANA/Desktop/Outliers_data.csv')

X = df.drop('MeanTemp', axis=1)
y = df[['MeanTemp']]
# Split train and test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1)
regression_model = LinearRegression()
regression_model.fit(X_train, y_train)
for idx, col_name in enumerate(X_train.columns):
    print("The coefficient for {} is {}".format(col_name, regression_model.coef_[0][idx]))

intercept = regression_model.intercept_[0]
print("The intercept is {}".format(intercept)) 
print('Score:' ,regression_model.score(X_test, y_test)) 

y_predict = regression_model.predict(X_test)
regression_model_mse = mean_squared_error(y_predict, y_test)
print('MSE:' , regression_model_mse)
print('MSE sqrt:' ,math.sqrt(regression_model_mse))  

#running a prediction test
print( 'The predicted Mean Temp is: ', (regression_model.predict([[2018, 3, 17, 4, 0, 2, 0]])))