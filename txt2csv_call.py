# -*- coding: utf-8 -*-
"""
Created on Thu Apr 12 09:47:10 2018

@author: jiangxingqi
"""
import cueb

#category_file_path = 'source/variety.txt'
#txt_path = 'data-text'

category_file_path = '/Sourcedata/Codetable/variety.txt'
txt_path = '/Sourcedata/Future/Day'

rs_csv_path = 'data-csv'

cueb.txt2csv.txt2csv_function(category_file_path, txt_path, rs_csv_path, "2018/6/1")

#cueb.txt2csv.txt2csv_function(category_file_path,'data-text','data-csv')