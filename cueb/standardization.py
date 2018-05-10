# -*- coding: utf-8 -*-
"""
Created on Thu Apr 12 09:47:10 2018

@author: jiangxingqi
"""
from scipy.stats import norm
import pandas as pd

'''
code_table_path: 码表文件路径
data_stand_path：数据标准化文件夹路径
data_csv_path：csv文件夹
'''
def standardizationFunction(code_table_path,data_csv_path,stand_path):
    dff = pd.read_csv(code_table_path, encoding='gbk', header=None)
    dff.sort_index(inplace=True)

    for i in range(len(dff.loc[:, 0])):
        # dff=np.array(dff)
        # print(dff[i])
        df = pd.read_csv(data_csv_path+'/%s.csv' % dff.iloc[i, 0], encoding='gbk')
        df.sort_index(inplace=True)

        # df=df.replace('None',0)
        # print(df)
        def norm_NM(Name):
            mid = df.loc[:, Name].median()
            # mid = np.median(df.loc[:,Name])
            qua = df.loc[:, Name].quantile(.75) - df.loc[:, Name].quantile(.25)
            norm_1 = (1 / 2) * ((df.loc[:, Name] - mid) / qua)
            df[Name] = (100 * norm.cdf(norm_1) - 50)

        ma_list = [5, 10, 20, 30, 40, 60]

        def MA(ma_list, Name):

            # 计算简单算术移动平均线MA - 注意：stock_data['close']为股票每天的收盘价
            for ma in ma_list:
                df['MA_' + str(ma)] = pd.rolling_mean(df[Name], ma)

                mid = df.loc[:, 'MA_' + str(ma)].median()
                # mid = np.median(df.loc[:,Name])
                qua = df.loc[:, 'MA_' + str(ma)].quantile(.75) - df.loc[:, 'MA_' + str(ma)].quantile(.25)
                norm_1 = (1 / 2) * ((df.loc[:, 'MA_' + str(ma)] - mid) / qua)
                df['MA_' + str(ma)] = (100 * norm.cdf(norm_1) - 60)

        def changeOfInventory(Name1):
            df['chicagliang1'] = df.loc[:, Name1].shift(1)
            df['chicangliangbianhua'] = df.loc[:, Name1] - df.loc[:, 'chicagliang1']

        # 资金变动=持仓量*今日收盘价
        def movementOfFunds(Name1, Name2):
            df['zijinbiandong'] = df.loc[:, Name1] * df.loc[:, Name2]

        # 收盘涨跌幅度
        def upAndDownClose(Name1, Name2):
            df['zhangdiefu_shoupanjia'] = (df.loc[:, Name1] / df.loc[:, Name2])
            # 分类（0或1）

        # 涨跌幅(结算价)
        def settlementPriceFluctuation(Name1, Name2):
            df['zhangdiefu_jiesuanjia'] = (df.loc[:, Name1] / df.loc[:, Name2])

        def classify(Name1, Name2):
            df['fenlei'] = df.loc[:, Name1] - df.loc[:, Name2]
            for i in range(len(df['fenlei'])):
                if df.loc[i, 'fenlei'] > 0:
                    df.loc[i, 'fenlei'] = 1
                else:
                    df.loc[i, 'fenlei'] = 0

        def contributionPrice(Name1, Name2):
            # df['价格变动贡献度']=(df.loc[:,Name1]/df.loc[:,Name2])*1000
            df['jiagebiandonggongxiandu'] = (df.loc[:, Name1] / df.loc[:, Name2])

        def max_min(Name1):

            N_max = df.loc[:, Name1].max()
            N_min = df.loc[:, Name1].min()
            df[Name1] = (df.loc[:, Name1] - N_min) / (N_max - N_min)

        def std_mean(Name2):
            N_std = df.loc[:, Name2].std()  # np.mean(df.loc[:,Name2], axis=0)#  df.loc[:,Name2].std()
            N_mean = df.loc[:, Name2].mean()  # np.mean(df.loc[:,Name2], axis=0)  #df.loc[:,Name2].mean()
            df[Name2] = (N_std - N_mean) / N_std

        # changeOfInventory('持仓量')
        upAndDownClose('zhangdie_shoupanjia', 'qianshoupan')
        contributionPrice('zhangdie_shoupanjia', 'shoupanjia')
        movementOfFunds('chicangliangbianhua', 'shoupanjia')
        settlementPriceFluctuation('zhangdie_jiesuanjia', 'qianjiesuanjia')
        norm_NM("kaipanjia")
        norm_NM("zuigaojia")
        norm_NM("zuidijia")
        norm_NM("zuidijia")
        norm_NM("qianshoupan")
        norm_NM("qianjiesuanjia")
        norm_NM("jiesuanjia")

        MA(ma_list, 'shoupanjia')
        norm_NM('zhangdiefu_jiesuanjia')
        norm_NM('zhangdiefu_shoupanjia')
        norm_NM('chicangliangbianhua')
        norm_NM('zijinbiandong')
        norm_NM('jiagebiandonggongxiandu')
        classify('shoupanjia', 'qianshoupan')

        df = df.loc[:,
             ['heyue', 'riqi', 'qianshoupan', 'kaipanjia', 'zuigaojia', 'zuidijia', 'shoupanjia', 'chengjiaoliang',
              'chengjiaoe', 'chengjiaobishu', 'zhangdie_shoupanjia',
              'zhangdiefu_shoupanjia', 'zhengfu_shoupanjia', 'junjia', 'chicangliang', 'qianjiesuanjia', 'jiesuanjia',
              'zhangdie_jiesuanjia', 'zhangdiefu_jiesuanjia',
              'zuijinjiaoyiriqi', 'shichangzuijinjiaoyiri', 'MA_5', 'MA_10', 'MA_20', 'MA_30', 'MA_40', 'MA_60',
              'chicangliangbianhua', 'zijinbiandong',
              'jiagebiandonggongxiandu', 'fenlei']]
        df = df.fillna(0)
        df.to_csv(stand_path+'/%s.csv' % dff.iloc[i, 0], encoding='gbk', index=False)