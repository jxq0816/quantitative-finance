# -*- coding: utf-8 -*-
"""
Created on Thu Apr 12 10:55:16 2018

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
    df=pd.read_csv('stand/%s.csv'%dff.iloc[i,0],encoding='gbk')
    df.sort_index(inplace=True)
    #print(df)
    df = df.loc[:,['MA_5','MA_10','MA_20','MA_30','MA_40','MA_60','持仓量变化','资金变动','价格变动贡献度','分类']]
   
    df.to_csv('index/%s.csv'%dff.iloc[i,0],encoding='gbk',index=False)