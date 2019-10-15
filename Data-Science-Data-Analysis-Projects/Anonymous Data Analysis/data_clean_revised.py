# -*- coding: utf-8 -*-
"""
Gia G
Data Scientist assessment
Methods are used to preprocess data.
"""
import pandas as pd
import numpy as np
weekdays=['mon','tues','wed','thur','fri']
months=['jan','feb','mar','apr','may','jun','jul','aug','sept','oct','nov','dec']

def fix_date_string(date_string, date_list):
    if not isinstance(date_string, str):
        return date_string
    date_string = date_string.lower()
    for s in date_list:
        if date_string.find(s) != -1:
            value=s
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

def encode_categorical_data(df):
    from sklearn.preprocessing import OneHotEncoder
    import numpy as np
    a = df
    size = len(a.columns)
    new_df = pd.DataFrame()
    for i in range(size):
        one_hot_encoder = OneHotEncoder(categories='auto', sparse=False)
        ohe = one_hot_encoder.fit_transform(np.array(a[i]).reshape(-1, 1))
        encoded_df = pd.DataFrame(ohe)
        new_df = pd.concat([new_df, encoded_df], axis=1)
    return pd.DataFrame(new_df)

#Fix numeric columns with $, commas, and/or % characters
#Make day of week column consistent
def parse_columns(pddf):
    columns=['x41','x45']
    for i in columns:
        pddf[i]=pddf[i].map(lambda x: parse_data(x))

def parse_categorical_data(df):
    #Convert all categorical data to lower case for consistencey
    for i in range(len(df.columns)):
        df[i]=df[i].str.lower()
    #Fix day of week and month strings for consistency
    df[1]=df[1].map(lambda x: fix_date_string(x, weekdays))
    #Change 'dev' to 'dec'
    df[2]=df[2].map(lambda x: fix_month(x))
    df[2]=df[2].map(lambda x: fix_date_string(x, months))
    return df
    
#Fix month that is labeled as 'dev' instead of 'dec'
def fix_month(x):
    if x=='dev':
        return 'dec'
    return x
