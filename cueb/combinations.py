# -*- coding: utf-8 -*-
"""
Created on Thu Apr 12 10:01:34 2018

@author: jiangxingqi
"""
from __future__ import division
import pandas as pd
import numpy as np
from  sklearn.model_selection import train_test_split
import csv
from itertools import combinations
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier

def combinationFunction(data_source_path,index_path,rs_path,function_name,test_size_param):
    dff = pd.read_csv(data_source_path, header=None)
    dff.sort_index(inplace=True)
    # 文件遍历
    for f in range(len(dff.loc[:, 0])):
        # 读取文件
        with open(index_path+'/%s.csv' % dff.iloc[f, 0]) as csvfile:
            # 分割
            readCSV = csv.reader(csvfile, delimiter=',')
            # 获得迭代器的下一个项目
            next(readCSV)
            X = []
            y = []
            for row in readCSV:
                # 读取指标到X
                X.append(np.array(row[0:len(row[:]) - 1]))
                # 读取标签到
                y.append(float(row[-1]))
        #划为数组
        X = np.array(X)
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size_param)
        #训练集X
        X_train = np.array(X_train)
        #训练集Y
        y_train = np.array(y_train)
        #测试集X
        X_test = np.array(X_test)
        #测试集
        y_test = np.array(y_test)

        x_test = []
        x_test = np.array(x_test)

        index_len = len(X_train[0])
        # 输出指标的个数
        print("\n")
        print("处理%s.csv" % dff.iloc[f, 0])
        print("指标个数:"+str(index_len))
        hashMap = {}
        # 排列组合遍历
        for i in range(1, index_len + 1):
            # 生成集合个数为i的组合
            print("开始处理%s个指标的组合" %i)
            combins = [c for c in combinations(range(index_len), i)]
            print(combins)
            # 组合的个数
            comLen = len(combins)
            print("组合个数%s" %comLen)

            # 当前排列进行遍历
            for j in range(comLen):
                # 对当前数组中的数进行赋值
                print("------------------------")
                print(combins[j])
                # 初始化训练集
                x_train = np.zeros(shape=(len(X_train[:, 0]), i))
                # 初始化测试集
                x_test = np.zeros(shape=(len(X_test[:, 0]), i))

                for k in range(len(combins[j])):
                    # print(len(X_train[:,combins[j][k]]))
                    # for m in range(len(X_train[:,0])):
                    # print(X_train[m,combins[j][k]])

                    x_train[:, k] = X_train[:, combins[j][k]]
                    x_test[:, k] = X_test[:, combins[j][k]]

                if(function_name == 'DecisionTreeClassifier'):
                    clf = DecisionTreeClassifier().fit(x_train, y_train)
                if(function_name == 'KNeighborsClassifier'):
                    clf = KNeighborsClassifier().fit(x_train, y_train)
                if(function_name == 'GaussianNB'):
                    clf = GaussianNB().fit(x_train, y_train)
                if(function_name == 'LogisticRegression'):
                    clf = LogisticRegression().fit(x_train, y_train)
                if (function_name == 'RandomForestClassifier'):
                    clf = RandomForestClassifier().fit(x_train, y_train)

                a = clf.predict(x_test)

                s = 0
                for ii in range(0, len(y_test)):
                    #print(str(a[ii])+"->"+str(y_test[ii]))
                    if a[ii] == y_test[ii]:
                        s = s + 1
                        #print(s)
                test_len=len(y_test)
                print("测试数据个数%s" %test_len)
                print("命中数据个数%s" %s)
                rate = s / test_len
                if rate >= 0.75:
                    print("命中比例%s" %rate)
                    # 将combins[j]：rate 存入hashMap
                    hashMap[combins[j]] = rate
                del (x_train)
                del (x_test)
                #end of j
                #break
            #end of i
            #break
        # 转为数组
        items = hashMap.items()
        # 数组排序
        sortedItems = sorted(items, key=lambda x: x[1], reverse=True)
        # print(sortedItems)
        rs = pd.DataFrame(sortedItems)
        rs.to_csv(rs_path+'/%s.csv' % dff.iloc[f, 0], encoding='gbk', index=False)
        #end of f
    print("The end")