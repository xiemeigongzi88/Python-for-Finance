# -*- coding: utf-8 -*-
"""
Created on Mon Jul  8 07:50:00 2019

@author: sxw17
"""


# 6. Getting all company pricing data in the S&P 500
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


def save_sp500_tickers():
    response= requests.get('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')
    soup= bs.BeautifulSoup(response.text)
    
    table=soup.find('table',{'class':"wikitable sortable"})
    tickers=[]
    
    for row in table.findAll('tr')[1:]:
        ticker=row.findAll('td')[0].text
        # 
        ticker=ticker[:-1]
        tickers.append(ticker)
        
    with open('sp500tickers.pickle','wb') as f:
        pickle.dump(tickers,f)

    print(tickers)
    return tickers

save_sp500_tickers()

with open ('sp500tickers.pickle', 'rb')  as f:
    content = pickle.load(f)

print('ATVI' in content)  # True 


def get_data_from_yahoo(reload_sp500=False):
    if reload_sp500:
        tickers=save_sp500_tickers()
        
    else:
        with open('sp500tickers.pickle','rb') as f:
            tickers=pickle.load(f)
    
    if not os.path.exists('stock_dfs'):
        os.makedirs('stock_dfs')
        
    start=dt.datetime(2000,1,1)
    end= dt.datetime(2019, 7,5)
    
    for ticker in tickers:
        if not os.path.exists('stock_dfs/{}.csv'.format(ticker)):
            df=web.DataReader(ticker,'yahoo', start, end)
            df.to_csv('stock_dfs/{}.csv'.format(ticker))
        else:
            print("Already have {}".format(ticker))
            
get_data_from_yahoo()

###########################################
with open ('sp500tickers.pickle', 'rb')  as f:
    companies = pickle.load(f)
    
print('ATVI' in companies)
companies.remove('ATVI')
print('ATVI' in companies) # False
companies.remove('ALLE')
companies.remove('GOOGL')
companies.remove('AMZN')
companies.remove('AEE')
companies.remove('AIV')
companies.remove('APTV')
companies.remove('BAC')
companies.remove('BRK.B')
companies.remove('BIIB')
companies.remove('BKNG')
companies.remove('BSX')
companies.remove('BMY')

def get_data_from_yahoo():
    tickers=companies
    
    if not os.path.exists('stock_dfs'):
        os.makedirs('stock_dfs')
        
    start=dt.datetime(2000,1,1)
    end= dt.datetime(2019, 7,5)
    
    for ticker in tickers:
        if not os.path.exists('stock_dfs/{}.csv'.format(ticker)):
            df=web.DataReader(ticker,'yahoo', start, end)
            df.to_csv('stock_dfs/{}.csv'.format(ticker))
        else:
            print("Already have {}".format(ticker))
            
get_data_from_yahoo()


#################################################################################3

























