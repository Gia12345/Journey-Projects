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
"""
import calendar
airline['Month'] = airline['Month'].apply(lambda x: calendar.month_abbr[x])
airline.head()
"""
def fix_date_string(date_string, date_list):
    if not isinstance(date_string, str):
        return date_string
    date_string = date_string.lower()
    for s in date_list:
        if date_string.find(s) != -1:
            value=s
    return value

def replace_null_values(x, strategy):
    from sklearn.impute import SimpleImputer
    imputer = SimpleImputer(missing_values=np.nan,strategy=strategy)
    imputer = imputer.fit(x)
    x = imputer.transform(x)
    x = pd.DataFrame.from_records(x)
    return x

def encode_categorical_data(df):
    return pd.get_dummies(df, prefix=df.columns, drop_first=True)

def parse_columns(df):
    #Fix numeric columns with $, commas, and/or % characters  
    #X41 US currency
    df['x41']=df['x41'].str.replace('$', '').astype(float)  
    #x45 Percentages
    df['x45']=(df['x45'].str.replace('%', '').astype(float))/100

def parse_categorical_data(df):
    #Convert all categorical data to lower case for consistencey
    df=df.apply(lambda x: x.str.lower())

    #Fix day of week and month strings for consistency
    df.iloc[:, 1]=df.iloc[:, 1].map(lambda x: fix_date_string(x, weekdays))
    #Change 'dev' to 'dec'
    df.iloc[:, 2]=df.iloc[:, 2].map(lambda x: fix_month(x))
    df.iloc[:, 2]=df.iloc[:, 2].map(lambda x: fix_date_string(x, months))
    return df
    
#Fix month that is labeled as 'dev' instead of 'dec'
def fix_month(x):
    if x=='dev':
        return 'dec'
    return x
