# -*- coding: utf-8 -*-
"""
Created on Thu Apr 12 09:47:10 2018

@author: jiangxingqi
"""
from scipy.stats import norm
import pandas as pd

'''
code_table_path: 码表文件路径
feature_path_path：指标文件夹路径
data_csv_path：csv文件夹
'''
def featureCalFunction(code_table_path,data_csv_path,feature_path):
    dff = pd.read_csv(code_table_path, encoding='gbk', header=None)
    dff.sort_index(inplace=True)

    for i in range(len(dff.loc[:, 0])):
        # dff=np.array(dff)
        # print(dff[i])
        df = pd.read_csv(data_csv_path+'/%s.csv' % dff.iloc[i, 0], encoding='gbk')
        df.sort_index(inplace=True)

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
            df['chicangliang1'] = df.loc[:, Name1].shift(1)
            df['chicangliangbianhua'] = df.loc[:, Name1] - df.loc[:, 'chicangliang1']

        # step 3资金变动=持仓量*今日收盘价
        def movementOfFunds(Name1, Name2):
            df['zijinbiandong'] = df.loc[:, Name1] * df.loc[:, Name2]
            #print(df['zijinbiandong'])

        # step1 收盘涨跌幅度 'zhangdie_shoupanjia', 'qianshoupan'
        def upAndDownClose(Name1, Name2):
            df['zhangdiefu_shoupanjia'] = (df.loc[:, Name1] / df.loc[:, Name2])
            #print(df['zhangdiefu_shoupanjia'])

        # 涨跌幅(结算价)
        def settlementPriceFluctuation(Name1, Name2):
            df['zhangdiefu_jiesuanjia'] = (df.loc[:, Name1] / df.loc[:, Name2])
            #print(df['zhangdiefu_jiesuanjia'])

        def classify(Name1, Name2):
            df['fenlei'] = df.loc[:, Name1] - df.loc[:, Name2]
            for i in range(len(df['fenlei'])):
                if df.loc[i, 'fenlei'] > 0:
                    df.loc[i, 'fenlei'] = 1
                else:
                    df.loc[i, 'fenlei'] = 0
        # step2 计算价格变动贡献度
        def contributionPrice(Name1, Name2):
            # df['价格变动贡献度']=(df.loc[:,Name1]/df.loc[:,Name2])*1000
            df['jiagebiandonggongxiandu'] = (df.loc[:, Name1] / df.loc[:, Name2])
            #print(df['jiagebiandonggongxiandu'])


        def max_min(Name1):

            N_max = df.loc[:, Name1].max()
            N_min = df.loc[:, Name1].min()
            #N_max - N_min==0 需要判断
            df[Name1] = (df.loc[:, Name1] - N_min) / (N_max - N_min)

        def std_mean(Name2):
            N_std = df.loc[:, Name2].std()  # np.mean(df.loc[:,Name2], axis=0)#  df.loc[:,Name2].std()
            N_mean = df.loc[:, Name2].mean()  # np.mean(df.loc[:,Name2], axis=0)  #df.loc[:,Name2].mean()
            # N_std==0 判断
            df[Name2] = (df.loc[:,Name2] - N_mean) / N_std

        #changeOfInventory('chicangliang')

        # 1计算收盘涨跌幅度
        # 涨跌（收盘价）前收盘
        upAndDownClose('zhangdie_shoupanjia', 'qianshoupan')

        # 2计算价格变动贡献度
        # '涨跌(收盘价)', '收盘价'
        contributionPrice('zhangdie_shoupanjia', 'shoupanjia')

        # 3资金变动=持仓量*今日收盘价
        # '持仓量变化', '收盘价'
        movementOfFunds('chicangliangbianhua', 'shoupanjia')

        # 4涨跌幅(结算价)
        # '涨跌(结算价)', '前结算价'
        settlementPriceFluctuation('zhangdie_jiesuanjia', 'qianjiesuanjia')

        # 5收盘价
        MA(ma_list, 'shoupanjia')

        # 6收盘价 前收盘
        classify('shoupanjia', 'qianshoupan')
        # 合约 日期 前收盘 开盘价 最高价 最低价 收盘价 成交量
        #  成交额 成交笔数 涨跌(收盘价)
        # 成交金额', '涨跌(收盘价),'均价', '持仓量', '前结算价', '结算价',
        # '涨跌(结算价)', '涨跌幅(结算价)'
        # '最近交易日期', '市场最近交易日', 'MA_5', 'MA_10', 'MA_20', 'MA_30', 'MA_40', 'MA_60',
        # '持仓量变化', '资金变动',
        # '价格变动贡献度', '分类'
        df = df.loc[:,
             ['heyue', 'riqi','qianshoupan', 'kaipanjia', 'zuigaojia', 'zuidijia', 'shoupanjia', 'chengjiaoliang',
              'chengjiaoe', 'chengjiaobishu', 'zhangdie_shoupanjia',
              'zhangdiefu_shoupanjia', 'zhengfu_shoupanjia', 'junjia', 'chicangliang', 'qianjiesuanjia', 'jiesuanjia',
              'zhangdie_jiesuanjia', 'zhangdiefu_jiesuanjia',
              'zuijinjiaoyiriqi', 'shichangzuijinjiaoyiri', 'MA_5', 'MA_10', 'MA_20', 'MA_30', 'MA_40', 'MA_60',
              'chicangliangbianhua', 'zijinbiandong',
              'jiagebiandonggongxiandu', 'fenlei']]
        df = df.fillna(0)
        df.to_csv(feature_path+'/%s.csv' % dff.iloc[i, 0], encoding='gbk', index=False)
        break