# -*- coding: utf-8 -*-
"""
Created on Tue Jul  9 08:54:13 2019

@author: sxw17
"""

# 12. ML 


import os 
os.getcwd()
os.chdir('C:\\Users\\sxw17\\Desktop\\python learning\\Python for Finance\\Python_Programming_for_Finance')

from collections import Counter
import pandas as pd 
import numpy as np 
import pickle

from sklearn import svm, cross_validation, neighbors
from sklearn.ensemble import VotingClassifier, RandomForestClassifier


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
    
    #df=df[['XOM', 'XOM_per_chg','XOM_target']]
    print(df)
    
    return x, y , df

# extract_feature_sets('XOM')

def do_ml(ticker):
    X, y, df = extract_feature_sets(ticker)

    X_train, X_test, y_train, y_test = cross_validation.train_test_split(X, y, test_size=0.25)

    clf = VotingClassifier([('lsvc', svm.LinearSVC()),
                            ('knn', neighbors.KNeighborsClassifier()),
                            ('rfor', RandomForestClassifier())])

    clf.fit(X_train, y_train)
    confidence = clf.score(X_test, y_test)
    print('accuracy:', confidence)
    predictions = clf.predict(X_test)
    print('predicted class counts:', Counter(predictions))
    print()
    print()
    return confidence


# examples of running:
do_ml('XOM')
do_ml('AAPL')
do_ml('ABT')
    



