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

#import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import GaussianNB
from sklearn import tree
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import roc_auc_score, accuracy_score, confusion_matrix
from sklearn.model_selection import cross_val_score, cross_val_predict
from sklearn.preprocessing import MinMaxScaler
from sklearn.pipeline import Pipeline
from process_data import process_train_data

#Load and process training data
training_data = 'data/exercise_02_train.csv'
train_x, train_y=process_train_data(training_data)
train_x=train_x.iloc[:10000,:]
train_y=train_y.iloc[:10000]

#Divide train and test data to test various methods
x_train, x_test, y_train, y_test = train_test_split(train_x, train_y, test_size=0.20)

#Test models

#Use scaling for Logistic Regression and K Nearest Neighbor

#Scaling data
scaler = MinMaxScaler()
x_train = scaler.fit_transform(x_train, y_train)
x_test = scaler.transform(x_test)

#Logistic Regression (use MinMaxScaler)
model=LogisticRegression(solver='liblinear')
model.fit(x_train, y_train) 
y_pred=model.predict(x_test)
y_prob = model.predict_proba(x_test)[:,1]
acc = accuracy_score(y_test, y_pred)
print('--------------- ','Log Regression for ')
print('Roc auc:  ' + str(roc_auc_score(y_test, y_pred)))
print('Accuracy score:  '+ str(acc))
cvs = cross_val_score(estimator=model, X=x_train, y=y_train, cv=10, scoring='roc_auc')
print('Cross Val Score Mean:  ', cvs.mean())
print('Cross Val Score std:  ', cvs.std())

y_pred=cross_val_predict(model, x_train, y_train, cv=10)
print('Roc auc:  ' + str(roc_auc_score(y_test, y_pred)))


#K Nearest Neighbor

params={'n_neighbors': [1, 10, 100]}
model = KNeighborsClassifier(n_neighbors=10)
model= GridSearchCV(model, param_grid=params, cv=10)
model.fit(x_train, y_train) 
y_pred=model.predict(x_test)
y_prob = model.predict_proba(x_test)[:,1]
acc = accuracy_score(y_test, y_pred)
print('--------------- ','KNeighborsClassifier for ', model.best_params_)
print('Roc auc:  ' + str(roc_auc_score(y_test, y_pred)))
print('Accuracy score:  '+ str(acc))
cvs=cross_val_score(estimator=model, X=x_train, y=y_train, cv=10, scoring='roc_auc')
print('Cross Val Score Mean:  ', cvs.mean())
print('Cross Val Score std:  ', cvs.std())

#Scaling not necessary

#GaussianNB
model = GaussianNB()
model.fit(x_train, y_train) 
y_pred=model.predict(x_test)
y_prob = model.predict_proba(x_test)[:,1]
acc = accuracy_score(y_test, y_pred)
print('--------------- ','GaussianNB')
print('Roc auc:  ' + str(roc_auc_score(y_test, y_pred)))
print('Accuracy score:  '+ str(acc))
cvs = cross_val_score(estimator=model, X=x_train, y=y_train, cv=10)
print('Cross Val Score Mean:  ', cvs.mean())
print('Cross Val Score std:  ', cvs.std())

#Decision Tree Classifier
params={'min_samples_split': [10, 50, 100, 150, 500], 'n_estimators':[]}
model = tree.DecisionTreeClassifier()
model= GridSearchCV(model, param_grid=params, cv=5)
model.fit(x_train, y_train) 
y_pred=model.predict(x_test)
y_prob = model.predict_proba(x_test)[:,1]
acc = accuracy_score(y_test, y_pred)
print('--------------- ','Decision Tree Classifier for ', model.best_params_)
print('Roc auc:  ' + str(roc_auc_score(y_test, y_pred)))
print('Accuracy score:  '+ str(acc))

# Try ensemble models

#Voting Classifier
from sklearn.ensemble import VotingClassifier, BaggingClassifier
log_clf=LogisticRegression()
knn_clf=KNeighborsClassifier()
dt_clf=tree.DecisionTreeClassifier()
model=VotingClassifier(estimators=[('lr', log_clf), 
                                   ('kn', knn_clf), 
                                   ('dt', dt_clf)], voting='soft')
model.fit(x_train, y_train)
y_pred=model.predict(x_test)
acc=accuracy_score(y_test, y_pred)
print('--------------', 'VotingClassifier')
print('Roc auc:  ' + str(roc_auc_score(y_test, y_pred)))
print('Accuracy score:  '+ str(acc))

#Bagging Classifier
model=BaggingClassifier(estimators=[('lr', log_clf), 
                                   ('kn', knn_clf), 
                                   ('dt', dt_clf)], voting='soft')
model.fit(x_train, y_train)
y_pred=model.predict(x_test)
acc=accuracy_score(y_test, y_pred)
print('--------------', 'VotingClassifier')
print('Roc auc:  ' + str(roc_auc_score(y_test, y_pred)))
print('Accuracy score:  '+ str(acc))