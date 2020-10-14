# -*- coding: utf-8 -*-
"""
Gia G
Data Scientist assessment
Final code
Used Voting Classifier and Logistic Regression to produce probablities 
after testing various methods including K Nearest Neighbor, Decision Tree, and
Random Forests and comparing metric ROC AUC.
Training file includes x values (100 features) and y value (target 0 or 1).  
Testing file includes only x values (100 features).
Predicted probabilites of each model are output to csv files.
"""
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import VotingClassifier, RandomForestClassifier
from sklearn import tree
from sklearn.externals import joblib
from process_data import process_train_data, process_test_data
from sklearn.preprocessing import MinMaxScaler

#Training file with x values (100 features) and y values (0 or 1)
training_data = 'data/exercise_02_train.csv'
train_x, train_y=process_train_data(training_data)

#Testing file with x values (100 features) and no y values
test_data = 'data/exercise_02_test.csv'
test_x=process_test_data(test_data)

#Scaling data
scaler = MinMaxScaler()
train_x = scaler.fit_transform(train_x, train_y)
test_x = scaler.transform(test_x)

#Part 1 Create and save models.
#Create Logistic Regression model
lr=LogisticRegression(solver='lbfgs', max_iter=5000)
lr_model = lr.fit(train_x,train_y)

#Create Voting Classfication model
#parameters determined by previous testing in 'model tests revised.py'
log_clf=LogisticRegression(solver='liblinear')
knn_clf=KNeighborsClassifier(n_neighbors=9, metric='manhattan')
dt_clf=tree.DecisionTreeClassifier(criterion='entropy', min_samples_split=114)
rf_clf=RandomForestClassifier(max_depth=20,n_estimators=30)
vc=VotingClassifier(estimators=[('lr', log_clf), 
                                   ('kn', knn_clf), 
                                   ('dt', dt_clf),
                                   ('rf', rf_clf)], 
    voting='soft')
vc_model=vc.fit(train_x, train_y)

#Save Logistic Regression model
filename1 = 'model_1.sav'
joblib.dump(lr_model, filename1)

#Save Voting Class model
filename2 = 'model_2.sav'
joblib.dump(vc_model, filename2)

#Part 2 Load and apply models
#Load the models
load_lr_model = joblib.load(filename1)
load_vc_model = joblib.load(filename2)

#Apply models
lr_prob = load_lr_model.predict_proba(test_x)[:,1]
vc_prob = load_vc_model.predict_proba(test_x)[:,1]

#Save predicted probabilities to files
np.savetxt('results1.csv', lr_prob, fmt="%.8f")
np.savetxt('results2.csv', vc_prob, fmt="%.8f")



