# -*- coding: utf-8 -*-
"""
Created on Mon Jul  8 02:38:20 2019

@author: sxw17
"""

# 5. Automating getting s&p 500 list 

import os 
os.getcwd()
os.chdir('C:\\Users\\sxw17\\Desktop\\python learning\\Python for Finance\\Python_Programming_for_Finance')


import bs4 as bs 
import pickle 
import requests

'''
response= requests.get('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')
soup= bs.BeautifulSoup(response.text,"lxml")
    
table=soup.find('table',{'class':"wikitable sortable"})
table.prettify()
tickers=[]
    
for row in table.findAll('tr')[1:]:
    tickers=row.findAll('td')[1].text
'''


def save_sp500_tickers():
    response= requests.get('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')
    soup= bs.BeautifulSoup(response.text)
    
    table=soup.find('table',{'class':"wikitable sortable"})
    tickers=[]
    
    for row in table.findAll('tr')[1:]:
        ticker=row.findAll('td')[0].text
        ticker=ticker[:-1]
        tickers.append(ticker)
        
    with open('sp500tickers.pickle','wb') as f:
        pickle.dump(tickers,f)

    print(tickers)
    return tickers

save_sp500_tickers()


# check 

with open('sp500tickers.pickle', 'rb') as pickle_file:
    content = pickle.load(pickle_file)
