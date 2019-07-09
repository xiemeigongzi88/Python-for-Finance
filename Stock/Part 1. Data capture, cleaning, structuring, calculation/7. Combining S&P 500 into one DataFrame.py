# -*- coding: utf-8 -*-
"""
Created on Mon Jul  8 11:58:55 2019

@author: sxw17
"""

# 7. Combining S&P 500 into one DataFrame
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



def save_sp500_tickers():
    response= requests.get('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')
    soup= bs.BeautifulSoup(response.text)
    
    table=soup.find('table',{'class':"wikitable sortable"})
    tickers=[]
    
    for row in table.findAll('tr')[1:]:
        ticker=row.findAll('td')[0].text
        
        ticker=ticker[:-1]
        '''
        mapping=str.maketrans(".","-")
        ticker=ticker.translate(mapping)
        '''
        ticker=str(ticker).replace('.','-')
        tickers.append(ticker)
        
    with open('sp500tickers.pickle','wb') as f:
        pickle.dump(tickers,f)

    print(tickers)
    return tickers

save_sp500_tickers()




def compile_data():
    with open('sp500tickers.pickle','rb') as f:
        tickers=pickle.load(f)
        
    main_df=pd.DataFrame()
    
    for count, ticker in enumerate(tickers):
        df = pd.read_csv('stock_dfs/{}.csv'.format(ticker))
        df.set_index('Date',inplace=True)
        
        df.rename(columns={'Adj Close': ticker}, inplace=True)
        df.drop(['Open','High','Low','Close','Volume'], axis=1, inplace=True)
        
        if main_df.empty:
            main_df=df
        else:
            main_df=main_df.join(df, how='outer')
            
        if count % 10 ==0:
            print(count)
        
    print(main_df)
    main_df.to_csv('sp500_joined_closed.csv')
    


compile_data()

