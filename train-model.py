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
from sklearn.linear_model import LogisticRegression

dff = pd.read_csv("data-text/sc.txt",header=None)
dff.sort_index(inplace=True)

for f in range(len(dff.loc[:,0])):
    with open(r'index/%s.csv'%dff.iloc[f,0],encoding="gbk") as csvfile:
         readCSV = csv.reader(csvfile, delimiter=',')  
         hearder=next(readCSV)
         X = []  
         y = []      
         for row in readCSV:  
         #print(len(row[:]))
            X.append(np.array(row[0:len(row[:])-1]))
            y.append(float(row[-1])) 
           
    X=np.array(X)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3) 
    X_train=np.array(X_train)
    y_train=np.array(y_train)
    X_test=np.array(X_test)
    y_test=np.array(y_test)

    x_test=[]
    x_test=np.array(x_test)

    com=len(X_train[0])
    suMM=0
    print("品种%s"%dff.iloc[f,0])
    #排列组合
    combination=[]
    accuracy=[]
    outputResult={}
    for i in range(1,com+1):
        combins = [c for c in  combinations(range(com), i)]
        comLen=len(combins)
        suMM+=comLen
       
        #当前排列进行遍历
        for j in range(comLen):
        #对当前数组中的数进行赋值
            
            
            x_train=np.zeros(shape=(len(X_train[:,0]),i))
            x_test=np.zeros(shape=(len(X_test[:,0]),i))
            for k in range(len(combins[j])):
            #print(combins[j])
            #print(len(X_train[:,combins[j][k]]))
            #for m in range(len(X_train[:,0])):
            
            #print(X_train[m,combins[j][k]])
                x_train[:,k]=X_train[:,combins[j][k]]
                x_test[:,k]=X_test[:,combins[j][k]]
                
            clf = LogisticRegression(penalty='l2',dual=False,tol=0.0001,C=1.0,fit_intercept=True,intercept_scaling=1,
                                     class_weight="balanced").fit(x_train, y_train)  
            a=clf.predict(x_test)
            s=0
            for ii in range(0,len(y_test)):
                if a[ii]==y_test[ii]:
                    s=s+1
                
            #print ("组合：",combins[j])
            #print(s/len(y_test))
            #print('-----')
           
            combination.append(combins[j])
            accuracy.append(s/len(y_test))
            del(x_train)
            del(x_test)
    outputResult={'组合':combination,
                      '准确率':accuracy}
    dfff=pd.DataFrame(outputResult)
    dfff.to_csv('result/%sresult.csv'%dff.iloc[f,0],encoding='gbk',index=False)    
    print(suMM)
        