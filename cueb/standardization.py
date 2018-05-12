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
'''
def standardizationFunction(code_table_path,data_csv_path,stand_path):
    dff = pd.read_csv(code_table_path, encoding='gbk', header=None)
    dff.sort_index(inplace=True)

    for i in range(len(dff.loc[:, 0])):

        df = pd.read_csv(data_csv_path+'/%s.csv' % dff.iloc[i, 0], encoding='gbk')

        print('start %s' % dff.iloc[i, 0])
        df.sort_index(inplace=True)

        def norm_NM(Name):
            print(" norm %s start" %Name)
            mid = df.loc[:, Name].median()
            qua = df.loc[:, Name].quantile(.75) - df.loc[:, Name].quantile(.25)
            df[Name] = (1.0 / 2) * ((df.loc[:, Name] - mid) / qua)

        #开盘价
        norm_NM("kaipanjia")
        #最高价
        norm_NM("zuigaojia")
        #最低价
        norm_NM("zuidijia")
        #收盘价
        norm_NM("shoupanjia")
        #前收盘
        norm_NM("qianshoupan")
        #前结算价
        norm_NM("qianjiesuanjia")
        #结算价
        norm_NM("jiesuanjia")
        #涨跌幅(结算价)
        norm_NM('zhangdiefu_jiesuanjia')
        #涨跌幅(收盘价)
        norm_NM('zhangdiefu_shoupanjia')
        #持仓量变化
        norm_NM('chicangliangbianhua')
        #资金变动
        norm_NM('zijinbiandong')
        #价格变动贡献度
        norm_NM('jiagebiandonggongxiandu')
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
        df.to_csv(stand_path+'/%s.csv' % dff.iloc[i, 0], encoding='gbk', index=False)