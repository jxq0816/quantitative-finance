# -- coding: UTF-8 --
import cueb

#code_file_path = "/Sourcedata/Codetable/variety.txt"
#souce_data_path = "/Sourcedata/Future/Day"

code_file_path = "source/variety.txt"
souce_data_path = "data-text"


# 将text文件转为CSV文件
cueb.txt2csv.txt2csv_function(code_file_path,souce_data_path,'data-csv')
print ("将text文件转为CSV文件 end")

# 指标的计算
cueb.indexCalculate.index_cal_function(code_file_path, 'data-csv', 'feature')
print ("指标的计算 end")

# 指标标准化
cueb.standardization.standardization_function(code_file_path,'feature','stand',2)
print ("指标标准化 end")

# 指标抽取
cueb.indexExtract.index_extract_function(code_file_path,'stand','index')
print ("指标抽取 end")

# 训练模型
cueb.combinations.combination_function(code_file_path,'index','result/rs-decision-tree','DecisionTreeClassifier',0.3,0.75)
print ("训练模型 end")