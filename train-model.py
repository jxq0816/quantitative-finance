# -- coding: UTF-8 --

import cueb

code_file_path = "source/variety.txt"
#code_file_path="/Sourcedata/Codetable/variety.txt"


#cueb.combinations.combinationFunction(code_file_path,'index','result/rs-bagging','BaggingClassifier',0.3,0.75)
#极端随机树
#cueb.combinations.combinationFunction(code_file_path,'index','result/rs-extra-tree','ExtraTreesClassifier',0.75)
#随机森林
#cueb.combinations.combinationFunction(code_file_path,'index','result/rs-random-forest','RandomForestClassifier',0.75)
# 决策树
cueb.combinations.combination_function(code_file_path,'index','result/rs-decision-tree','DecisionTreeClassifier',0.3,0.75)
#KNN
#cueb.combinations.combinationFunction(code_file_path,'index','result/rs-knn','KNeighborsClassifier',0.3,0.75)
#贝叶斯
#cueb.combinations.combinationFunction(code_file_path,'index','result/rs-naive-bayes','GaussianNB',0.75)
#逻辑回归
#cueb.combinations.combinationFunction(code_file_path,'index','result/rs-logistic-regression','LogisticRegression',0.75)
