# -*- coding: utf-8 -*-
"""
Created on Thu Apr 12 09:47:10 2018

@author: jiangxingqi
"""
import cueb

#cueb.index_calculate.index_cal_function('source/variety.txt', 'data-csv', 'feature')


code_file_path = "/Sourcedata/Codetable/variety.txt"

data_csv_path = "data-csv"

feature_path = "feature"

cueb.index_calculate.index_cal_function(code_file_path, data_csv_path, feature_path)