# -*- coding: utf-8 -*-
"""
Created on Tue Jul  9 00:51:51 2019

@author: sxw17
"""

# 11. Creating labels fro ML

import os 
os.getcwd()
os.chdir('C:\\Users\\sxw17\\Desktop\\python learning\\Python for Finance\\Python_Programming_for_Finance')

from collections import Counter
import pandas as pd 
import numpy as np 
import pickle


def process_data_for_labels(ticker):
    hm_days=5 
    
    df= pd.read_csv('sp500_joined_closed.csv', index_col=0)
    
    tickers=df.columns.values.tolist()
    
    df.fillna(0, inplace=True)
    
    # percent change for the past five days 
    df['{}_per_chg'.format(ticker)]= (df[ticker].shift(-5) - df[ticker])/df[ticker]
    
    df.fillna(0, inplace=True)
    
    return tickers, df


# deal with the labels 
def buy_sell_hold(*args):
    columns_list=[c for c in args]
    
    requirement=0.02
    
    for c in columns_list:
        if c > requirement:
            return 1 
        elif c< requirement:
            return -1 
        else:
            return 1 
        
def extract_feature_sets(ticker):
    tickers, df = process_data_for_labels(ticker)
    
    df['{}_target'.format(ticker)]= list(map(buy_sell_hold, df['{}_per_chg'.format(ticker)]))
    
    values =  df['{}_target'.format(ticker)].values.tolist()
    str_values=[str(i) for i in values]

    print("Data Spread: ", Counter(str_values))
    
    df.fillna(0, inplace=True)
    df= df.replace([np.inf, -np.inf], np.nan)
    df.dropna(inplace=True)
    
    df_values= df[[tticker for tticker in tickers]].pct_change()
    df_values= df_values.replace([np.inf, -np.inf], 0)
    df_values.fillna(0, inplace=True)

    x= df_values.values
    y=df['{}_target'.format(ticker)].values
    
    df=df[['XOM', 'XOM_per_chg','XOM_target']]
    print(df)
    
    return x, y , df

extract_feature_sets('XOM')



#######################################################################
# test by single one 

hm_days=5 
    
df= pd.read_csv('sp500_joined_closed.csv', index_col=0)
    
tickers=df.columns.values.tolist()
    
df.fillna(0, inplace=True)

df.isnull()

ticker='XOM' 
    # percent change for the past five days 
df['{}_per_chg'.format(ticker)]= (df[ticker].shift(-5) - df[ticker])/df[ticker]
    
df.fillna(0, inplace=True)
    
df['{}_per_chg'.format(ticker)]= (df[ticker].shift(-5) - df[ticker])/df[ticker]
    
df.fillna(0, inplace=True)


    
df['{}_target'.format(ticker)]= list(map(buy_sell_hold, df['{}_per_chg'.format(ticker)]))
    
values =  df['{}_target'.format(ticker)].values.tolist()

str_values=[str(i) for i in values]

print("Data Spread: ", Counter(str_values))

df.isnull().values # all are False 

df.fillna(0, inplace=True)


df= df.replace([np.inf, -np.inf], np.nan)
df.dropna(inplace=True)
    
df_values= df[[ticker for ticker in tickers]].pct_change()
df_values= df_values.replace([np.inf, -np.inf], 0)
df_values.fillna(0, inplace=True)

x= df_values.values
y=df['{}_target'.format(ticker)].values
    

