# -*- coding: utf-8 -*-
"""
@author: Gia
Moved SVC test to a separate file because it caused kernal to need restart
"""
import pandas as pd
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import roc_auc_score, accuracy_score, classification_report
from data_clean import parse_columns, encode_categorical_data
from data_clean import replace_null_values
from sklearn.model_selection import GridSearchCV
from sklearn.feature_selection import SelectPercentile

trd = r'C:\Users\Gia\Project X\exercise_02_train.csv'

train_pd=pd.read_csv(trd) 
train_x = train_pd.loc[:,:'x99']
train_y = train_pd.loc[:,'y']
parse_columns(train_x)

#Replace null values
train_x = replace_null_values(train_x)

#Encoding categorical data
train_x = encode_categorical_data(train_x)

print('select percentile 10')
selector = SelectPercentile(percentile=10)
selector.fit(train_x, train_y)
train_x = selector.transform(train_x)

#Divide train and test data to test various methods
x_train, x_test, y_train, y_test = train_test_split(train_x, train_y, test_size=0.10)

#StandardScaler to rescale features x
scaler = StandardScaler()
x_train = scaler.fit_transform(x_train)
x_test = scaler.transform(x_test)

#PCA
from sklearn.decomposition import PCA
pca = PCA(n_components=2)
x_train = pca.fit_transform(x_train)
x_test = pca.transform(x_test)
explain_var= pca.explained_variance_ratio_

#Using GridSearchCV to find the best parameters for SVC
parameters = [{'C':[1,10,100,1000], 'kernel':['linear']},
               {'C':[1,10,100,1000], 'kernel':['rbf'], 
                'gamma':[.5,.1,.01,.001,.0001]}]
grid_search = GridSearchCV(estimator=SVC(), param_grid=parameters,
                           scoring='accuracy', cv=10, n_jobs=-1)
grid_search = grid_search.fit(x_train, y_train)
best_ac = grid_search.best_score_
best_param = grid_search.best_params_

svm_predictions = grid_search.predict(x_test)
svm_prob = grid_search.predict_proba(x_test)[:,1]
svm_acc = accuracy_score(y_test, svm_predictions)
print(roc_auc_score(y_test, svm_predictions))
print('SVC accuracy:  '+ str(svm_acc))
print(classification_report(y_test, svm_predictions))
