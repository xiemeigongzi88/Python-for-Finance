# -*- coding: utf-8 -*-
"""
Created on Tue Jul  2 00:45:57 2019

@author: sxw17
"""

# 3. Basic Stock Data Manipulation 
import os 
os.getcwd()
os.chdir('C:\\Users\\sxw17\\Desktop\\python learning\\Python_Data\\Data Analysis with Pandas')



import datetime as dt
import matplotlib.pyplot as plt 
from matplotlib import style 
import pandas as pd 

import fix_yahoo_finance as fy  
fy.pdr_override() 

from pandas.api.types import is_list_like

import pandas as pd
pd.core.common.is_list_like = pd.api.types.is_list_like

import pandas_datareader.data as web 

style.use('ggplot')

start=dt.datetime(2000,1,1)
end=dt.datetime(2019, 6, 30)

#df= web.DataReader('TLSA','yahoo', start, end)

df=pd.read_csv('tsla.csv', index_col=0, parse_dates=True )

print(df.head(100))
#  100 day rolling moving average
# this will take the current price, and the prices from the past 99 days, add them up,
# divide by 100, and there's your current 100-day moving average. 
df['100ma']=df['Adj Close'].rolling(window=100, min_periods=0).mean()


print(df.head(100))

df.dropna(inplace=True)

print(df.head())

print(df.tail())

ax1=plt.subplot2grid((6,1),(0,0), rowspan=5, colspan=1)
ax2=plt.subplot2grid((6,1),(5,0), rowspan=1, colspan=1, sharex=ax1)

ax1.plot(df.index, df['Adj Close'])
ax1.plot(df.index, df['100ma'])
ax2.plot(df.index, df['Volume'])

plt.legend()
plt.show()

