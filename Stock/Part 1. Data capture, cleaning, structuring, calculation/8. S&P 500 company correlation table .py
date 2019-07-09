# -*- coding: utf-8 -*-
"""
Created on Mon Jul  8 12:39:31 2019

@author: sxw17
"""

# 8. S&P 500 company correlation table 
import os 
os.getcwd()
os.chdir('C:\\Users\\sxw17\\Desktop\\python learning\\Python for Finance\\Python_Programming_for_Finance')

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

def visualize_data():
    df=pd.read_csv('sp500_joined_closed.csv')
    '''
    df['AAPL'].plot()
    plt.show()
    '''
    df_corr=df.corr()
    print(df_corr.head())
    
    data=df_corr.values # numpy.ndarray
    
    fig=plt.figure()
    ax= fig.add_subplot(1,1,1)
    
    heat_map=ax.pcolor(data,cmap=plt.cm.RdYlGn)
    fig.colorbar(heat_map)
    ax.set_xticks(np.arange(data.shape[0])+0.5, minor=False)
    ax.set_yticks(np.arange(data.shape[1])+0.5, minor=False)
    ax.invert_yaxis()
    
visualize_data()
