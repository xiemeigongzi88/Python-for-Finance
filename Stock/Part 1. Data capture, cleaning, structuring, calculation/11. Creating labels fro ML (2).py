# -*- coding: utf-8 -*-
"""
Created on Mon Jul  8 21:42:27 2019

@author: sxw17
"""

# 11. Creating labels fro ML
import os 
os.getcwd()
os.chdir('C:\\Users\\sxw17\\Desktop\\python learning\\Python for Finance\\Python_Programming_for_Finance')

import quandl
import pandas as pd 
import bs4 as bs 
import pickle 
import requests
import datetime as dt
import pandas as pd 

import fix_yahoo_finance as fy  
fy.pdr_override() 

from pandas.api.types import is_list_like

pd.core.common.is_list_like = pd.api.types.is_list_like

import pandas_datareader.data as web 
import fix_yahoo_finance as yf 
from pandas_datareader import data as pdr
yf.pdr_override()

import numpy as np 
import matplotlib.pyplot as plt 
from matplotlib import style 
style.use('ggplot')



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


def buy_sell_hold(*args):
    cols=[c for c in args]
    
    requirement=0.02 
    
    for col in cols:
        if col>requirement:
            return 1
        elif col<requirement:
            return -1 
        else:
            return 0 
        
        
from collections import Counter

def extract_featuresets(ticker):
    tickers, df= process_data_for_labels(ticker)
    
    df['{}_target'.format(ticker)] = list(map( buy_sell_hold,
                                               df['{}_1d'.format(ticker)],
                                               df['{}_2d'.format(ticker)],
                                               df['{}_3d'.format(ticker)],
                                               df['{}_4d'.format(ticker)],
                                               df['{}_5d'.format(ticker)],
                                               df['{}_6d'.format(ticker)],
                                               df['{}_7d'.format(ticker)] ))
    
    vals = df['{}_target'.format(ticker)].values.tolist()
    str_vals = [str(i) for i in vals]
    print('Data spread:',Counter(str_vals))
    
    df.fillna(0, inplace=True)
    df = df.replace([np.inf, -np.inf], np.nan)
    df.dropna(inplace=True)
    
    df_vals=df[[ticker for ticker in tickers ]].pct_change()
    X = df_vals.values
    y = df['{}_target'.format(ticker)].values

    return X,y,df
        
#######################################################################
# test 
    '''
hm_days=7 
df= pd.read_csv('sp500_joined_closed.csv', index_col=0)
tickers=df.columns.values.tolist()
df.fillna(0, inplace=True)
 
ticker='AAPL'   
for i in range(1, hm_days+1):
    print(i)
        
    df['{}_{}d'.format(ticker,i)]=(df[ticker].shift(-i)-df[ticker])/df[ticker]
        
df.fillna(0, inplace=True)
    
 #   return tickers,df     

df['{}_target'.format(ticker)] = list(map( buy_sell_hold,
                                               df['{}_1d'.format(ticker)],
                                               df['{}_2d'.format(ticker)],
                                               df['{}_3d'.format(ticker)],
                                               df['{}_4d'.format(ticker)],
                                               df['{}_5d'.format(ticker)],
                                               df['{}_6d'.format(ticker)],
                                               df['{}_7d'.format(ticker)] ))
    
# args=list(df['AAPL_1d'],df['AAPL_2d'],df['AAPL_3d'],df['AAPL_4d'],df['AAPL_5d'],df['AAPL_6d'],df['AAPL_7d'])




vals = df['{}_target'.format(ticker)].values.tolist()
str_vals = [str(i) for i in vals]
print('Data spread:',Counter(str_vals))
    
df.fillna(0, inplace=True)
df = df.replace([np.inf, -np.inf], np.nan)
df.dropna(inplace=True)
    
X = df_vals.values
y = df['{}_target'.format(ticker)].values

       
def buy_sell_hold(*args):
   #print(len(args))
    cols=[c for c in args]
    print(len(cols))
    
    requirement=0.02 
    
    for col in cols:
        if col>requirement:
            return 1
        elif col<requirement:
            return -1 
        else:
            return 0         
        
buy_sell_hold(df['AAPL_1d'],df['AAPL_2d'])

cols=[c for c in df['AAPL_1d']]
print(len(cols))

requirement=0.02 
    
cnt_0=0
cnt_pos=0
cnt_neg=0
for col in cols:
    if col>requirement:
        print(1)
        cnt_pos+=1
    elif col<requirement:
        print(-1)
        cnt_neg+=1
    else:
        print(0)
        cnt_0+=1

from collections import Counter
print(Counter(cols))
'''