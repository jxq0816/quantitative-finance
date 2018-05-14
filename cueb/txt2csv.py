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

        # 从左到右对列进行命名
        df = pd.read_csv(data_text_path+'/%s.txt' % dff.iloc[i, 0], parse_dates=True, names=['heyue', 'riqi', 'qianshoupan', 'kaipanjia',
                                                                                  'zuigaojia', 'zuidijia', 'shoupanjia', 'chengjiaoliang', 'chengjiaoe',
                                                                                  'chengjiaobishu', 'zhangdie_shoupanjia', 'zhangdiefu_shoupanjia',
                                                                                  'zhengfu_shoupanjia', 'junjia', 'chicangliang', 'chicangliangbianhua',
                                                                                  'qianjiesuanjia', 'jiesuanjia', 'zhangdie_jiesuanjia', 'zhangdiefu_jiesuanjia',
                                                                                  'zuijinjiaoyiriqi', 'shichangzuijinjiaoyiri'])
        df.sort_index(inplace=True)
        #print(df)
        df = df.replace('None', 0)
        for j in range(df.shape[0]):
            if df.loc[j, 'kaipanjia'] == 0:
                # print(df.shape[1])
                df = df.drop([j])
        df.to_csv(data_csv_path+'/%s.csv'%dff.iloc[i,0],encoding='gbk',index=False)