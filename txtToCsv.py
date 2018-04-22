# -*- coding: utf-8 -*-
"""
Created on Thu Apr 12 08:23:53 2018

@author: 王钊
"""

import pandas as pd
import numpy as np


dff = pd.read_csv("data-text/variety.txt",encoding='gbk',header=None)
dff.sort_index(inplace=True)

#print(dff)


#print(dff.iloc[11,0])
for i in range(len(dff.loc[:,0])):
    #dff=np.array(dff)
    #print(dff[i])
    df=pd.read_csv('data-text/%s.txt'%dff.iloc[i,0],parse_dates=True,names=['合约','日期','前收盘','开盘价',
                   '最高价','最低价','收盘价','成交量','成交额','成交笔数','涨跌(收盘价)','涨跌幅(收盘价)',
                   '振幅(收盘价)','均价','持仓量','持仓量变化','前结算价','结算价','涨跌(结算价)','涨跌幅(结算价)',
                   '最近交易日期','市场最近交易日'])
    df.sort_index(inplace=True)
    df=df.replace('None',0)
    #print(df)
    #del df['kong']
    df.to_csv('data-csv/%s.csv'%dff.iloc[i,0],encoding='gbk',index=False)
    
    