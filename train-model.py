# -*- coding: utf-8 -*-
"""
Created on Thu Apr 12 10:01:34 2018

@author: jiangxingqi
"""
import pandas as pd
import numpy as np  
from sklearn.cross_validation import train_test_split
import csv 
from itertools import combinations
from sklearn.tree import DecisionTreeClassifier

dff = pd.read_csv("data-text/sc.txt",header=None)
dff.sort_index(inplace=True)
#文件遍历
for f in range(len(dff.loc[:,0])):
    #读取文件
    with open(r'index/%s.csv'%dff.iloc[f,0],encoding='gbk') as csvfile:
         #分割
         readCSV = csv.reader(csvfile, delimiter=',')
         print(readCSV);
         #获得迭代器的下一个项目
         next(readCSV)
         X = []  
         y = []      
         for row in readCSV:  
            #读取指标到X
            X.append(np.array(row[0:len(row[:])-1]))
            #读取标签到
            y.append(float(row[-1]))

    X=np.array(X)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3)
    X_train=np.array(X_train)
    y_train=np.array(y_train)
    X_test=np.array(X_test)
    y_test=np.array(y_test)

    x_test=[]
    x_test=np.array(x_test)

    index_len=len(X_train[0])
    #输出指标的个数
    print(index_len)
    print("品种%s"%dff.iloc[f,0])

    hashMap = {}
    #排列组合遍历
    for i in range(1,index_len+1):
        #生成集合个数为i的组合
        combins = [c for c in  combinations(range(index_len), i)]
        #组合的个数
        comLen=len(combins)

        #当前排列进行遍历
        for j in range(comLen):
        #对当前数组中的数进行赋值

            #print(combins[j])
            #初始化训练集
            x_train=np.zeros(shape=(len(X_train[:,0]),i))
            #初始化测试集
            x_test=np.zeros(shape=(len(X_test[:,0]),i))

            for k in range(len(combins[j])):

                #print(len(X_train[:,combins[j][k]]))
                #for m in range(len(X_train[:,0])):
                    #print(X_train[m,combins[j][k]])

                x_train[:,k]=X_train[:,combins[j][k]]
                x_test[:,k]=X_test[:,combins[j][k]]

            clf = DecisionTreeClassifier().fit(x_train, y_train)
            a=clf.predict(x_test)
            #print(a)
            s=0
            for ii in range(0,len(y_test)):
                if a[ii]==y_test[ii]:
                    s=s+1

            rate = s / len(y_test)
            # 将combins[j]：rate 存入hashMap
            hashMap[combins[j]] = rate
            del(x_train)
            del(x_test)
    #转为数组
    items = hashMap.items()
    #数组排序
    sortedItems=sorted(items, key=lambda x:x[1], reverse=True)
    #print(sortedItems)
    rs=pd.DataFrame(sortedItems)
    rs.to_csv('result/%sresult.csv'%dff.iloc[f,0],encoding='gbk',index=False)
    break
print("The end")