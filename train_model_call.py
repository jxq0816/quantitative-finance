# -- coding: UTF-8 --
"""
Created on Thu Apr 12 09:47:10 2018

@author: jiangxingqi
"""
import cueb

category_file_path = "source/variety.txt"

#category_file_path = "/Sourcedata/Codetable/variety.txt"

index_path = "index"

rs_path = "result/rs-logistic-regression"

test_ratio = 0.3

hit_ratio = 0.75

classifier_function = "GaussianNB"



#cueb.combinations.combinationFunction(code_file_path,'index','result/rs-bagging','BaggingClassifier',0.3,0.75)
#极端随机树
#cueb.combinations.combinationFunction(code_file_path,'index','result/rs-extra-tree','ExtraTreesClassifier',0.75)
#随机森林
#cueb.combinations.combinationFunction(code_file_path,'index','result/rs-random-forest','RandomForestClassifier',0.75)
# 决策树
#cueb.train_model.train_model_function(category_file_path, index_path, rs_path, classifier_function, test_ratio, hit_ratio, 0)
#cueb.train_model.train_model_function(category_file_path, index_path, rs_path, classifier_function, test_ratio, hit_ratio, 1)
#KNN
#cueb.combinations.combinationFunction(code_file_path,'index','result/rs-knn','KNeighborsClassifier',0.3,0.75)
#贝叶斯
#cueb.combinations.combinationFunction(code_file_path,'index','result/rs-naive-bayes','GaussianNB',0.75)
#逻辑回归
cueb.train_model.train_model_function(category_file_path, index_path, rs_path, classifier_function, test_ratio, hit_ratio, 0)
cueb.train_model.train_model_function(category_file_path, index_path, rs_path, classifier_function, test_ratio, hit_ratio, 1)