# -*- coding: utf-8 -*-
"""
Created on Thu Apr 12 10:55:16 2018

@author: 王钊
"""

# step 3 ：指标抽取

import pandas as pd
import numpy as np

dff = pd.read_csv("source/variety.txt", encoding='gbk', header=None)
dff.sort_index(inplace=True)

# print(dff)


# print(dff.iloc[11,0])
for i in range(len(dff.loc[:, 0])):
    # dff=np.array(dff)
    # print(dff[i])
    filename = dff.iloc[i, 0]
    print(filename + " start")
    df = pd.read_csv('stand/%s.csv' % filename, encoding='gbk')
    df.sort_index(inplace=True)
    # print(df)
    df = df.loc[:, ['MA_5', 'MA_10', 'MA_20', 'MA_30', 'MA_40', 'MA_60', '持仓量变化', '资金变动', '价格变动贡献度', '分类']]

    df.to_csv('index/%s.csv' % filename, encoding='gbk', index=False)
print("The end")