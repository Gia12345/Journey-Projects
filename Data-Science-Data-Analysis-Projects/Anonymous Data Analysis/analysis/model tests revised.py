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

from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import GaussianNB
from sklearn import tree
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import roc_auc_score, accuracy_score, confusion_matrix
from sklearn.model_selection import cross_val_score
from sklearn.preprocessing import MinMaxScaler
from process_data import process_train_data
import matplotlib.pyplot as plt
import numpy as np

#Load and process training data
training_data = 'data/exercise_02_train.csv'
train_x, train_y=process_train_data(training_data)

#Subset data for testing purposes (shorter testing time)
train_x=train_x.iloc[:10000,:]
train_y=train_y.iloc[:10000]

#Divide train and test data to test various methods
x_train, x_test, y_train, y_test = train_test_split(train_x, train_y, 
                                                    test_size=0.25, 
                                                    stratify=train_y)

#Test models

#Use scaling for Logistic Regression and K Nearest Neighbor

#Scaling data
scaler = MinMaxScaler()
x_train = scaler.fit_transform(x_train, y_train)
x_test = scaler.transform(x_test)

#Logistic Regression (use scaled data)
model=LogisticRegression(solver='liblinear')
model.fit(x_train, y_train) 
y_pred=model.predict(x_test)
#y_prob = model.predict_proba(x_test)[:,1]
acc = accuracy_score(y_test, y_pred)
print('--------------- ','Log Regression for ')
print('Roc auc:  ' + str(roc_auc_score(y_test, y_pred)))
print('Accuracy score:  '+ str(acc))
cvs = cross_val_score(estimator=model, X=x_train, y=y_train, cv=4, scoring='roc_auc')
print('Cross Val Score Mean:  ', cvs.mean())
print('Cross Val Score std:  ', cvs.std())
print('Confusion matrix:  ', confusion_matrix(y_test, y_pred))

#y_pred=cross_val_predict(model, x_train, y_train, cv=10)
#print('Roc auc:  ' + str(roc_auc_score(y_test, y_pred)))


#K Nearest Neighbor (use scaled data)
accuracy = []
neighbors = list(range(9,29,2))

for m in ['manhattan', 'minkowski', 'euclidean']:
    accuracy = []
    for n in neighbors:    
        knn = KNeighborsClassifier (n_neighbors=n, metric=m)
        knn.fit(x_train,y_train)
        pred_i = knn.predict(x_test)
        accuracy.append(roc_auc_score(pred_i,y_test))
    
    plt.plot(neighbors, accuracy, marker='o')
    plt.xlabel('K')
    plt.ylabel('Roc Auc')
    plt.title(m)
    plt.show()

#kmodel = KNeighborsClassifier(n_neighbors=9, metric='manhattan')

params={'n_neighbors': neighbors,
          'metric':['minkowski','manhattan','euclidean']}
model=KNeighborsClassifier()
kmodel= GridSearchCV(model, param_grid=params, cv=4, scoring='roc_auc')

kmodel.fit(x_train, y_train) 
y_pred=kmodel.predict(x_test)
#y_prob = kmodel.predict_proba(x_test)[:,1]
acc = accuracy_score(y_test, y_pred)
print('--------------- ','KNeighborsClassifier for ')#, model.best_params_)
print('Roc auc:  ' + str(roc_auc_score(y_test, y_pred)))
print('Accuracy score:  '+ str(acc))
print('Confusion matrix:  ', confusion_matrix(y_test, y_pred))

#Scaling not necessary

#GaussianNB
model = GaussianNB()
model.fit(x_train, y_train) 
y_pred=model.predict(x_test)
#y_prob = model.predict_proba(x_test)[:,1]
acc = accuracy_score(y_test, y_pred)
print('--------------- ','GaussianNB')
print('Roc auc:  ' + str(roc_auc_score(y_test, y_pred)))
print('Accuracy score:  '+ str(acc))
cvs = cross_val_score(estimator=model, X=x_train, y=y_train, cv=4, scoring='roc_auc')
print('Cross Val Score Mean:  ', cvs.mean())
print('Cross Val Score std:  ', cvs.std())

#Decision Tree Classifier
params={'min_samples_split': list(range(110,120,1)), 
        'criterion':['entropy']}
model = tree.DecisionTreeClassifier()
model= GridSearchCV(model, param_grid=params, cv=4, scoring='roc_auc')
model.fit(x_train, y_train) 
y_pred=model.predict(x_test)
#y_prob = model.predict_proba(x_test)[:,1]
acc = accuracy_score(y_test, y_pred)
print('--------------- ','Decision Tree Classifier for ', model.best_params_)
print('Roc auc:  ' + str(roc_auc_score(y_test, y_pred)))
print('Accuracy score:  '+ str(acc))

# Try ensemble models

#RandomForest Classifier
from sklearn.ensemble import RandomForestClassifier
from matplotlib.legend_handler import HandlerLine2D

max_depths = np.linspace(1, 32, 32, endpoint=True)
train_results = []
test_results = []
for max_depth in max_depths:
   rf2=RandomForestClassifier(max_depth=max_depth,n_estimators=30)
   rf2.fit(x_train, y_train)
   train_pred = rf2.predict(x_train)
   f1_score1 = roc_auc_score(y_train,train_pred)
   train_results.append(f1_score1)

   y_pred = rf2.predict(x_test)
   f1_score1 = roc_auc_score(y_test,y_pred)
   test_results.append(f1_score1)
    
plt.figure(figsize=(10,10))
line1, = plt.plot(max_depths, train_results, 'b', label="Train Roc Auc-score")
line2, = plt.plot(max_depths, test_results, 'r', label="Test Roc Auc-score")
plt.legend(handler_map={line1: HandlerLine2D(numpoints=2)})
plt.ylabel('Roc AUC-score')
plt.xlabel('Tree depth')
plt.show()

params={'max_depth':[19,20,21,22], 'n_estimators':[25,30,35]}
model=RandomForestClassifier()
model=GridSearchCV(model, param_grid=params, cv=4, scoring='roc_auc')
model.fit(x_train, y_train)
y_pred=model.predict(x_test)
print('-----------------------Random Forest')
print('Roc auc:  ' + str(roc_auc_score(y_test, y_pred)))
acc = accuracy_score(y_test, y_pred)
print('Accuracy score:  '+ str(acc))


#Voting Classifier
#Scale data before processing
from sklearn.ensemble import VotingClassifier
log_clf=LogisticRegression(solver='liblinear')
knn_clf=KNeighborsClassifier(n_neighbors=9, metric='manhattan')
dt_clf=tree.DecisionTreeClassifier(criterion='entropy', min_samples_split=114)
rf_clf=RandomForestClassifier(max_depth=20,n_estimators=30)
model=VotingClassifier(estimators=[('lr', log_clf), 
                                   ('kn', knn_clf), 
                                   ('dt', dt_clf),
                                   ('rf', rf_clf)], 
    voting='soft')
model.fit(x_train, y_train)
y_pred=model.predict(x_test)
acc=accuracy_score(y_test, y_pred)
print('--------------', 'VotingClassifier')
print('Roc auc:  ' + str(roc_auc_score(y_test, y_pred)))
print('Accuracy score:  '+ str(acc))

