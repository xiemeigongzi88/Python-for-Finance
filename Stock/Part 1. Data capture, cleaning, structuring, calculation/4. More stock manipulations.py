# -*- coding: utf-8 -*-
"""
Created on Sun Jul  7 12:11:33 2019

@author: sxw17
"""

# 4. More stock manipulations
# resample()

import os 
os.getcwd()
os.chdir('C:\\Users\\sxw17\\Desktop\\python learning\\Python for Finance\\Python_Programming_for_Finance')


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
end=dt.datetime(2019, 7,5)

df= web.DataReader('TSLA','yahoo', start, end)
print(df.head())

df.to_csv('TSLA_stock.csv')

data=pd.read_csv('TSLA_stock.csv', parse_dates=True, index_col=0)

data_ohlc=data['Adj Close'].resample('10D').ohlc()
data_volumn=df['Volume'].resample('10D').sum()

print(data_ohlc.head())
print(data_volumn.head())

from mpl_finance import candlestick_ohlc
import matplotlib.dates as mdates


data_ohlc.reset_index(inplace=True)

data_ohlc['Date']= data_ohlc['Date'].map(mdates.date2num)

print(data_ohlc)

ax1=plt.subplot2grid((6,1), (0,0), rowspan=5, colspan=1)
# 把 mdates 转化为 正常的日期 
ax1.xaxis_date()

import numpy as np

# 画图
# matplotlib.finance.candlestick_ochl(ax, quotes, width=0.2, colorup='k', colordown='r', alpha=1.0
candlestick_ohlc(ax1, data_ohlc.values, width=2, colorup='g')

#填充两个函数之间的区域，使用fill_between函数
#plt.fill_between(x, y1, y2, facecolor = "yellow")

ax2=plt.subplot2grid((6,1),(5,0), rowspan=1, colspan=1, sharex=ax1)
ax2.fill_between(data_volumn.index.map(mdates.date2num), data_volumn.values,0)

plt.show()

