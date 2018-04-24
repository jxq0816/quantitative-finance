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
data_stand_path：数据标准化文件夹路径
data_index_path：数据指标抽取目标文件夹
'''
def indexExtractFunction(data_source_path,data_stand_path,data_index_path):
    dff = pd.read_csv(data_source_path, encoding='gbk', header=None)
    dff.sort_index(inplace=True)

    # print(dff)


    # print(dff.iloc[11,0])
    for i in range(len(dff.loc[:, 0])):
        # dff=np.array(dff)
        # print(dff[i])
        filename = dff.iloc[i, 0]
        print(filename + " start")
        df = pd.read_csv(data_stand_path+'/%s.csv' % filename, encoding='gbk')
        df.sort_index(inplace=True)
        # print(df)
        df = df.loc[:, ['MA_5', 'MA_10', 'MA_20', 'MA_30', 'MA_40', 'MA_60', '持仓量变化', '资金变动', '价格变动贡献度', '分类']]

        df.to_csv(data_index_path+'/%s.csv' % filename, encoding='gbk', index=False)
    print("The end")