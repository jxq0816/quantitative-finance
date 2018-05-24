# -*- coding: utf-8 -*-
"""
Created on Thu Apr 12 09:47:10 2018

@author: jiangxingqi
"""
import pandas as pd

'''
code_table_path: 码表文件路径
data_stand_path：数据标准化文件夹路径
data_csv_path：csv文件夹
stand_formula_type:标准化公式{1：4分距，2：最大最小方法，3：标准差方法}
'''
zero = 0.000000000001


def index_standardization_function(code_table_path, data_csv_path, stand_path,stand_formula_type):

    dff = pd.read_csv(code_table_path, encoding='gbk', header=None)
    dff.sort_index(inplace=True)

    for i in range(len(dff.loc[:, 0])):

        df = pd.read_csv(data_csv_path+'/%s.csv' % dff.iloc[i, 0], encoding='gbk')

        print('start norm %s' % dff.iloc[i, 0])
        df.sort_index(inplace=True)

        # InterQuartileRange 四分位距
        def iqr(Name):
            # print("start norm %s" %Name)
            mid = df.loc[:, Name].median()
            qua = df.loc[:, Name].quantile(.75) - df.loc[:, Name].quantile(.25)
            # print(qua)
            if abs(qua) > zero:
                df[Name] = (df.loc[:, Name] - mid) / qua
            else:
                print("skip norm %s" %Name)

        # 最大最小方法
        def max_min(Name1):

            N_max = df.loc[:, Name1].max()
            N_min = df.loc[:, Name1].min()
            # N_max - N_min==0 需要判断
            if abs(N_max - N_min) > zero:
                df[Name1] = (df.loc[:, Name1] - N_min) / (N_max - N_min)

        # 标准差方法
        def std_mean(Name2):
            N_std = df.loc[:, Name2].std()  # np.mean(df.loc[:,Name2], axis=0)#  df.loc[:,Name2].std()
            N_mean = df.loc[:, Name2].mean()  # np.mean(df.loc[:,Name2], axis=0)  #df.loc[:,Name2].mean()
            # N_std==0 判断
            # TODO
            if abs(N_mean) > zero:
                df[Name2] = (df.loc[:, Name2] - N_mean) / N_std

        # 开盘价 最高价 最低价 收盘价 前收盘
        list = ['kaipanjia', 'zuigaojia', 'zuidijia', 'shoupanjia','qianshoupan',
                # 前结算价 结算价 涨跌幅(结算价) 涨跌幅(收盘价) 持仓量变化
                'qianjiesuanjia','jiesuanjia','zhangdiefu_jiesuanjia','zhangdiefu_shoupanjia','chicangliangbianhua',
                # 资金变动 价格变动贡献度
                'zijinbiandong','jiagebiandonggongxiandu']
        if stand_formula_type == 1:
            for j in range(len(list)):
                iqr(list[j])

        if stand_formula_type == 2:
            for k in range(len(list)):
                max_min(list[k])

        if stand_formula_type == 3:
            for m in range(len(list)):
                std_mean(list[m])


        # 合约 日期 前收盘 开盘价 最高价 最低价 收盘价 成交量
        # 成交额 成交笔数 涨跌(收盘价)
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
        df.to_csv(stand_path+'/%s.csv' % dff.iloc[i, 0], encoding='gbk', index=False)