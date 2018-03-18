# -*- coding: utf-8 -*-
"""
Random Forrest Model

@author: Eran Biran
"""

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor

data = pd.read_csv('C:/Users/ERANA/Desktop/Outliers_data.csv')

labels = np.array(data['Total_Precip_mm'])
data= data.drop('Total_Precip_mm', axis = 1)

data_list = list(data.columns)
data = np.array(data)
# Split Training and Test
train_data, test_data, train_labels, test_labels = train_test_split(data, labels, test_size = 0.3)
# The baseline predictions based on historical means.
baseline_preds = test_data[:, data_list.index('MeanTemp')]

rf = RandomForestRegressor(n_estimators = 1000) # Instantiate model with 1000 decision trees
rf.fit(train_data, train_labels)# Train the model on training data
predictions = rf.predict(test_data)
errors = abs(predictions - test_labels)
mape = 100 * (errors / test_labels)# Calculate mean absolute percentage error
accuracy = 100 - np.mean(mape) #Accuracy in %
print('Accuracy:', round(accuracy, 2), '%.')# accuracy of model

importances = list(rf.feature_importances_) # Get variable importance
feature_importances = [(data, round(importance, 2)) for data, importance in zip(data_list, importances)]
feature_importances = sorted(feature_importances, key = lambda x: x[1], reverse = True) # List sorted
[print('Variable: {:20} Importance: {}'.format(*pair)) for pair in feature_importances]