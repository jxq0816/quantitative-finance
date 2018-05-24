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
cueb.index_calculate.index_cal_function(code_file_path, 'data-csv', 'feature')
print ("指标的计算 end")

# 指标标准化
cueb.index_standardization.index_standardization_function(code_file_path, 'feature', 'stand', 2)
print ("指标标准化 end")

# 指标抽取
cueb.index_extract.index_extract_function(code_file_path, 'stand', 'index')
print ("指标抽取 end")

# 训练模型
cueb.train_model.train_model_function(code_file_path, 'index', 'result/rs-decision-tree', 'DecisionTreeClassifier', 0.3, 0.75, 0)
cueb.train_model.train_model_function(code_file_path, 'index', 'result/rs-decision-tree', 'DecisionTreeClassifier', 0.3, 0.75, 1)
print ("训练模型 end")

# 总排序
cueb.result_sort.result_sort_function('source/variety.txt', 'result/rs-decision-tree/0', 'result/rs-decision-tree', '0')
cueb.result_sort.result_sort_function('source/variety.txt', 'result/rs-decision-tree/1', 'result/rs-decision-tree', '1')
print ("总排序 end")