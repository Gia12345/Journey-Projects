# -*- coding: utf-8 -*-
"""
Created on Wed Jun  3 15:16:19 2020

@author: Gia
"""
from data_clean_revised import parse_columns, encode_categorical_data
from data_clean_revised import replace_null_values, parse_categorical_data
import pandas as pd

def process_data(df):
    parse_columns(df)
    
    #Separate categorical data and numerical data
    num_columns=df.select_dtypes(include='float').columns
    cat_columns=df.select_dtypes(exclude='float').columns
    
    #Clean categorical data
    #categorical_data = parse_categorical_data(categorical_data)
    df[cat_columns]=parse_categorical_data(df[cat_columns])

    
    #Replace null values in both categorical data and numerical data
    df[cat_columns] = replace_null_values(df[cat_columns], 'most_frequent')
    df[num_columns] = replace_null_values(df[num_columns], 'mean')

    #Encoding categorical data
    cat_df=encode_categorical_data(df[cat_columns])
    df=df.drop(cat_columns, axis=1)
    
    #Unite categorical data and numerical data
    return pd.concat([df, cat_df], axis=1)

def process_train_data(filename):
    training_data = filename
    train_pd=pd.read_csv(training_data) 
    train_x = train_pd.loc[:,:'x99']
    train_y = train_pd.loc[:,'y']
    train_x=process_data(train_x)
    return train_x, train_y

def process_test_data(filename):
    test_data=filename
    test_df=pd.read_csv(test_data)
    test_x = test_df.loc[:,:'x99']
    return process_data(test_x)
