# -*- coding: utf-8 -*-
"""
Created on Thu Apr 12 09:47:10 2018

@author: jiangxingqi
"""
import cueb

code_file_path = "/Sourcedata/Codetable/variety.txt"

feature_path = "feature"

stand_path = "stand"

stand_type = 2

cueb.index_standardization.index_standardization_function(code_file_path, feature_path, stand_path, stand_type)

#cueb.index_standardization.index_standardization_function('source/variety.txt', 'feature', 'stand', 2)