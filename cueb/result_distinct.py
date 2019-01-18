# -*- coding: utf-8 -*-
"""
Created on Thu Apr 12 10:01:34 2018

@author:xingqijiang
"""
from __future__ import division
import pandas as pd
import os


'''
ascend_path:涨文件夹路径
decline_path：跌文件夹路径
rs_path：总存储路径
'''
zero = 0.000000000001


def result_distinct_function(ascend_path, decline_path, rs_path):
    ascend = pd.read_csv(ascend_path, encoding='gbk', header=None)
    decline = pd.read_csv(decline_path, encoding='gbk', header=None)
    ascend_rs = pd.DataFrame(columns=['category', 'combination', 'rate', 'trend'])
    cnt = 0
    ascend_dic = {}
    double_dic = {}
    for i in range(1, len(ascend.loc[:, 0])):

        ascend_category = ascend.iloc[i, 0]
        print(ascend_category)
        bool = 0
        for j in range(1, 11):
            decline_category = decline.iloc[j, 0]
            if ascend_category == decline_category:
                print(j)
                print("delete %s " % ascend_category)
                double_dic[ascend_category] = 1
                bool = 1
                break
        if bool == 0:
            print("valid %s" % ascend_category)
            ascend_dic[ascend_category] = 1
            cnt = cnt + 1
            ascend_rs.loc[cnt, 'category'] = ascend_category
            ascend_rs.loc[cnt, 'combination'] = ascend.loc[i, 1]
            ascend_rs.loc[cnt, 'rate'] = ascend.loc[i, 2]
            ascend_rs.loc[cnt, 'trend'] = ascend.loc[i, 3]

        if cnt >= 20:
            print("ascend end")
            break
    ascend_rs.to_csv(rs_path + '/ascent-sort.csv', encoding='gbk', index=False)
    print("decent----------------------------------------------------- ")
    decline_rs = pd.DataFrame(columns=['category', 'combination', 'rate', 'trend'])
    for k in range(1, len(decline.loc[:, 0])):

        decline_category = decline.iloc[k, 0]

        if ascend_dic.get(decline_category) == None and double_dic.get(decline_category) == None:

            print("valid %s" % decline_category)
            cnt = cnt + 1
            decline_rs.loc[cnt, 'category'] = decline_category
            decline_rs.loc[cnt, 'combination'] = decline.loc[k, 1]
            decline_rs.loc[cnt, 'rate'] = decline.loc[k, 2]
            decline_rs.loc[cnt, 'trend'] = decline.loc[k, 3]
        else:
            print("delete %s " % decline_category)

        if cnt >= 40:
            break
    decline_rs.to_csv(rs_path + '/decline-sort.csv', encoding='gbk', index=False)
    print("The end")