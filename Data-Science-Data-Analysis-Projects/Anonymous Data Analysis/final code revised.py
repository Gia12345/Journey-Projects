# -*- coding: utf-8 -*-
"""
Gia G
Data Scientist assessment
Final code
Used KNN and Logistic Regression to produce probablities after testing
various methods including Gaussian Naive Bayes, Decision Tree, and
Adaoboost.  
Training file includes x values (100 features) and y value (0 or 1).  
Testing file includes only x values (100 features).
Predicted probabilites of each model are output to csv files.
"""
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.externals import joblib
#from data_clean_revised import parse_columns, encode_categorical_data, replace_null_values
#from data_clean_revised import parse_categorical_data
from process_data import process_train_data, process_test_data
from sklearn.preprocessing import StandardScaler

#Training file with x values (100 features) and y values (0 or 1)
training_data = 'data/exercise_02_train.csv'
train_x, train_y=process_train_data(training_data)

#Testing file with x values (100 features) and no y values
test_data = 'data/exercise_02_test.csv'
test_x=process_test_data(test_data)

#Scaling data
scaler = StandardScaler()
train_x = scaler.fit_transform(train_x, train_y)
test_x = scaler.transform(test_x)

#Part 1 Create and save models.
#Create Logistic Regression model
lr=LogisticRegression(solver='lbfgs', max_iter=5000)
lr_model = lr.fit(train_x,train_y)

#Create KNN model
knn = KNeighborsClassifier(n_neighbors=3)
knn_model = knn.fit(train_x, train_y)

#Save Logistic Regression model
filename1 = 'model_1.sav'
joblib.dump(lr_model, filename1)

#Save KNN model
filename2 = 'model_2.sav'
joblib.dump(knn_model, filename2)

#Part 2 Load and apply models
#Load the models
load_lr_model = joblib.load(filename1)
load_knn_model = joblib.load(filename2)

#Apply models
lr_prob = load_lr_model.predict_proba(test_x)[:,1]
knn_prob = load_knn_model.predict_proba(test_x)[:,1]

#Save predicted probabilities to files
np.savetxt('results1.csv', lr_prob, fmt="%.8f")
np.savetxt('results2.csv', knn_prob, fmt="%.8f")



