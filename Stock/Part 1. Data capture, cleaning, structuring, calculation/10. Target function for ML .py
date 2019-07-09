# -*- coding: utf-8 -*-
"""
Created on Mon Jul  8 14:35:47 2019

@author: sxw17
"""

# 10. Target function for ML 
import numpy as np 
import pandas as pd 
import pickle

import os 
os.getcwd()
os.chdir('C:\\Users\\sxw17\\Desktop\\python learning\\Python for Finance\\Python_Programming_for_Finance')


def process_data_for_labels(ticker):
    hm_days=7 
    df= pd.read_csv('sp500_joined_closed.csv', index_col=0)
    tickers=df.columns.values.tolist()
    df.fillna(0, inplace=True)
    
    for i in range(1, hm_days+1):
        print(i)
        
        df['{}_{}d'.format(ticker,i)]=(df[ticker].shift(-i)-df[ticker])/df[ticker]
        
    df.fillna(0, inplace=True)
    
    return tickers,df 



