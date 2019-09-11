# -*- coding: utf-8 -*-
"""
Gia G
Data Scientist assessment
Methods are used to preprocess data.
"""
import pandas as pd
import numpy as np

def fix_day_of_week(data):
    value = data
    if data == 'wed':
        value = 'wednesday'
    if data == 'thur' or data == 'thurday':
        value = 'thursday'
    if data == 'friday':
        value = 'fri'    
    return value

def parse_data(data):
    value=data
    if value is not None and isinstance(value, str) and value is not '':
        if value[0] =='$':
            if len(value)>1:
                value = float(value.replace('$','').replace(',',''))
            else:
                value=0
        elif value[len(value)-1]=='%':
            value = float(value.replace('%',''))/100  
    return value

def replace_null_values(x, strategy):
    from sklearn.impute import SimpleImputer
    imputer = SimpleImputer(missing_values=np.nan,strategy=strategy)
    imputer = imputer.fit(x)
    x = imputer.transform(x)
    x = pd.DataFrame.from_records(x)
    return x

def encode_categorical_data(x):
    from sklearn.preprocessing import LabelEncoder, OneHotEncoder
    label_encoder = LabelEncoder()
    counts = [0]
    for i in range(4):
        x[i] = label_encoder.fit_transform(x[i].astype(str))
        counts.append(len(label_encoder.classes_)-1)
    for i in range(4):      
        one_hot_encoder = OneHotEncoder(categorical_features= [i+counts[i]])
        x = one_hot_encoder.fit_transform(x).toarray()
    return pd.DataFrame(x)

#Fix numeric columns with $, commas, and/or % characters
#Make day of week column consistent
def parse_columns(pddf):
    columns=['x41','x45']
    for i in columns:
        pddf[i]=pddf[i].map(lambda x: parse_data(x))
    pddf['x35']=pddf['x35'].map(lambda x: fix_day_of_week(x))
    
def get_categorical_data(pddf):
    return pddf.loc[:,['x34', 'x35', 'x68', 'x93']]
    
def get_numerical_data(pddf):
    return pd.concat([pddf.loc[:,:'x33'], 
                      pddf.loc[:,'x36':'x67'], 
                      pddf.loc[:,'x69':'x92'],
                      pddf.loc[:,'x94':'x99']], axis=1)
