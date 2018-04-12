# -*- coding: utf-8 -*-
"""
Created on Thu Apr 12 08:23:53 2018

@author: jiangxingqi
"""

import pandas as pd
import numpy as np


dff = pd.read_csv("data-text/sc.txt",header=None)
dff.sort_index(inplace=True)

#print(dff)


#print(dff.iloc[11,0])
for i in range(len(dff.loc[:,0])):
    #dff=np.array(dff)
    #print(dff[i])
    df=pd.read_csv('data-text/%s.txt'%dff.iloc[i,0],names=['合约','日期','前收盘','前结算','开盘价','最高价','最低价','收盘价','结算价','涨跌(收盘价)','涨跌(结算价)','成交量','成交金额','持仓量','kong'])
    df.sort_index(inplace=True)
    #print(df)
    del df['kong']
    df.to_csv('data-csv/%s.csv'%dff.iloc[i,0],encoding='gbk',index=False)