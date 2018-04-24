# -*- coding: utf-8 -*-
"""
Created on Thu Apr 12 08:23:53 2018

@author: jiangxingqi
"""

import pandas as pd
import numpy as np

#step 1：text ---> csv

'''
data_source_path:品类文件路径
data_text_path：数据源text文件夹路径
data_csv_path：数据CSV文件夹路径
'''
def txt2csvFunction(data_source_path,data_text_path,data_csv_path):
    dff = pd.read_csv(data_source_path,header=None)
    dff.sort_index(inplace=True)

    #print(dff)


    #print(dff.iloc[11,0])
    for i in range(len(dff.loc[:,0])):
        #dff=np.array(dff)
        #print(dff[i])
        df=pd.read_csv(data_text_path+'/%s.txt'%dff.iloc[i,0],names=['合约','日期','前收盘','前结算','开盘价','最高价','最低价','收盘价','结算价','涨跌(收盘价)','涨跌(结算价)','成交量','成交金额','持仓量','kong'])
        df.sort_index(inplace=True)
        #print(df)
        del df['kong']
        df.to_csv(data_csv_path+'/%s.csv'%dff.iloc[i,0],encoding='gbk',index=False)