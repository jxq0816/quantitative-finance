# -*- coding: utf-8 -*-
"""
Created on Thu Apr 12 10:01:34 2018

@author:xingqijiang
"""
from __future__ import division
import pandas as pd
import os


'''
code_table_path:数据源文件路径
trend_path：涨跌文件夹路径
rs_path：总排序存储路径
trend：【1：涨 0：跌】
'''
zero = 0.000000000001


def result_sort_function(code_table_path, trend_path, rs_path, trend):
    dff = pd.read_csv(code_table_path, encoding='gbk', header=None)
    dff.sort_index(inplace=True)
    all = pd.DataFrame(columns=['category', 'combination', 'rate', 'trend'])
    cnt=0
    for i in range(len(dff.loc[:, 0])):
        # dff=np.array(dff)
        category = dff.iloc[i, 0]
        file = trend_path+"/"+str(category)+".csv"
        #print file
        if os.path.exists(file):
            print("category %s" % category)
            df = pd.read_csv(trend_path+'/%s.csv' % category, encoding='gbk')
            df.sort_index(inplace=True)
            column_size=df.columns.size
            if column_size != 0:
                #for j in range(len(df.loc[:, 'combination'])):
                all.loc[cnt,'category'] = category
                all.loc[cnt,'combination'] = df.loc[0, 'combination']
                all.loc[cnt, 'rate'] = df.loc[0, 'rate']
                all.loc[cnt, 'trend'] = trend
                cnt = cnt+1
    all = all.sort_values(by='rate',ascending=False)
    all.to_csv(rs_path + '/sort'+trend+'.csv', encoding='gbk', index=False)
    print("The end")