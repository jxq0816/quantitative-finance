# -*- coding: utf-8 -*-
"""
Created on Thu Apr 12 10:01:34 2018

@author:王钊
"""
from __future__ import division
import pandas as pd
import os
from pandas.core.frame import DataFrame


'''
code_table_path:数据源文件路径
trend_path：分类文件夹路径
'''
zero = 0.000000000001


def union_category_function(code_table_path, trend_path, rs_path, trend):
    dff = pd.read_csv(code_table_path, encoding='gbk', header=None)
    dff.sort_index(inplace=True)
    all = pd.DataFrame(columns=['category', 'combination', 'rate', 'trend'])
    cnt=0
    for i in range(len(dff.loc[:, 0])):
        # dff=np.array(dff)
        category = dff.iloc[i, 0]
        file = trend_path+"/"+category+".csv"
        print file
        if os.path.exists(file):
            print("union category %s" % category)
            df = pd.read_csv(trend_path+'/%s.csv' % category, encoding='gbk')
            df.sort_index(inplace=True)
            column_size=df.columns.size
            if column_size != 0:
                for j in range(len(df.loc[:, 'combination'])):
                    all.loc[cnt,'category'] = category
                    all.loc[cnt,'combination'] = df.loc[j, 'combination']
                    all.loc[cnt, 'rate'] = df.loc[j, 'rate']
                    all.loc[cnt, 'trend'] = trend
                    cnt = cnt+1
    all.sort_values(by='rate', axis=0, ascending=False)
    all.to_csv(rs_path + '/all'+trend+'.csv', encoding='gbk', index=False)
    print("The end")