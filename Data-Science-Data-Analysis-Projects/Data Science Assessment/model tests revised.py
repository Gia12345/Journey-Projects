# -*- coding: utf-8 -*-
"""
Gia G
Data Scientist assessment
Testing code
This is testing different methods on the training data by dividing 
the training data into two sets - train and test.
The two methods with the best scores will be used in the final code
with the given training and testing files.
"""

import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import GaussianNB
from sklearn import tree
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import roc_auc_score, accuracy_score
from sklearn.ensemble import AdaBoostClassifier
from data_clean_revised import parse_columns, encode_categorical_data
from data_clean_revised import replace_null_values, parse_categorical_data
from sklearn.model_selection import cross_val_score
from sklearn.preprocessing import StandardScaler

trd = r'C:\Users\Gia\Project X\exercise_02_train.csv'

train_pd=pd.read_csv(trd) 
train_x = train_pd.loc[:,:'x99']
train_y = train_pd.loc[:,'y']
parse_columns(train_x) 

#Separate categorical data and numerical data
numerical_data=train_x.select_dtypes(include='float')
categorical_data=train_x.select_dtypes(exclude='float')

#Replace null values in both categorical data and numerical data
categorical_data = replace_null_values(categorical_data, 'most_frequent')
categorical_data = parse_categorical_data(categorical_data)
numerical_data = replace_null_values(numerical_data, 'mean')

#Encoding categorical data
categorical_data = encode_categorical_data(categorical_data)

#Unite categorical data and numerical data
train_x = pd.concat([categorical_data, numerical_data], axis=1)

#Divide train and test data to test various methods
x_train, x_test, y_train, y_test = train_test_split(train_x, train_y, test_size=0.10)

#Scaling data
scaler = StandardScaler()
x_train = scaler.fit_transform(x_train, y_train)
x_test = scaler.transform(x_test)

#ADD GRIDSEARCH TO FIND THE BEST VALUES FOR MODELS

log_regr=LogisticRegression(solver='lbfgs', max_iter=5000)
log_regr.fit(x_train, y_train) 
test_y_logpred=log_regr.predict(x_test)
log_prob = log_regr.predict_proba(x_test)[:,1]
log_acc = accuracy_score(y_test, test_y_logpred)
print('Roc auc:  ' + str(roc_auc_score(y_test, test_y_logpred)))
print('Log Regression accuracy:  '+ str(log_acc))
log_accuracies = cross_val_score(estimator=log_regr, X=x_train, y=y_train, cv=10)
print(log_accuracies.mean())
print(log_accuracies.std())

g = GaussianNB()
g.fit(x_train, y_train) 
test_y_gpred=g.predict(x_test)
gau_prob = g.predict_proba(x_test)[:,1]
gau_acc = accuracy_score(y_test, test_y_gpred)
print('Roc auc:  ' + str(roc_auc_score(y_test, test_y_gpred)))
print('Gaussian NB accuracy:  '+ str(gau_acc))
gau_accuracies = cross_val_score(estimator=g, X=x_train, y=y_train, cv=10)
print(gau_accuracies.mean())
print(gau_accuracies.std())

dt = tree.DecisionTreeClassifier(min_samples_split=10)
dt.fit(x_train, y_train) 
test_y_dpred=dt.predict(x_test)
dt_prob = dt.predict_proba(x_test)[:,1]
dt_acc = accuracy_score(y_test, test_y_dpred)
print('Roc auc:  ' + str(roc_auc_score(y_test, test_y_dpred)))
print('Decision tree accuracy:  '+ str(dt_acc))
print('DT=10')

n = KNeighborsClassifier(n_neighbors=10)
n.fit(x_train, y_train)
test_y_npred = n.predict(x_test)
n_prob = n.predict_proba(x_test)[:,1]
n_acc = accuracy_score(y_test, test_y_npred)
print('Roc auc:  ' + str(roc_auc_score(y_test, test_y_npred)))
print('KNN accuracy:  '+ str(n_acc))
print('Knn=10')
"""
n_accuracies = cross_val_score(estimator=n, X=x_train, y=y_train, cv=10)
print(n_accuracies.mean())
print(n_accuracies.std())
"""

ab = AdaBoostClassifier()
ab.fit(x_train, y_train) 
predictions = ab.predict(x_test)
ab_acc = accuracy_score(y_test, predictions)
print('Roc auc:  ' + str(roc_auc_score(y_test, predictions)))
print('Adaboost accuracy:  '+ str(ab_acc))
ab_accuracies = cross_val_score(estimator=ab, X=x_train, y=y_train, cv=10)
print(ab_accuracies.mean())
print(ab_accuracies.std())
