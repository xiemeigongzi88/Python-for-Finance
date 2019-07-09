# -*- coding: utf-8 -*-

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
end=dt.datetime(2019,6,30)

# comment ctrl+1 
##df=web.DataReader("TSLA",'yahoo', start, end)
#df = web.DataReader('TSLA','yahoo',start, end)
#
##df= web.DataReader('TSLA','yahoo', start, end)
#
#
##df.to_csv('tsla.csv')

df_web= web.DataReader('TSLA','yahoo', start, end)
print(df_web.head())

df_web.to_csv('tsla.csv')

df_read=pd.read_csv('tsla.csv', parse_dates=True, index_col=0)

'''
index_col : int or sequence or False, default None
用作行索引的列编号或者列名，如果给定一个序列则有多个行索引。
如果文件不规则，行尾有分隔符，则可以设定index_col=False 来是的pandas不适用第一列作为行索引。

parse_dates : boolean or list of ints or names or list of lists or dict, default False
boolean. True -> 解析索引
list of ints or names. e.g. If [1, 2, 3] -> 解析1,2,3列的值作为独立的日期列；
list of lists. e.g. If [[1, 3]] -> 合并1,3列作为一个日期列使用
dict, e.g. {‘foo’ : [1, 3]} -> 将1,3列合并，并给合并后的列起名为"foo"
'''

print(df_read.head())

df_read.plot()

df_read['Adj Close'].plot()

plt.show()

print(df_read['Adj Close'])


print(df_read[['Open','High']].head())




















