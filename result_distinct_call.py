# -- coding: UTF-8 --
"""
Created on Thu Apr 12 09:47:10 2018

@author: jiangxingqi
"""

import cueb


trend_0_path = 'result/rs-logistic-regression/sort0.csv'

trend_1_path = 'result/rs-logistic-regression/sort1.csv'

out_path = 'result/rs-logistic-regression'


cueb.result_distinct.result_distinct_function(trend_1_path, trend_0_path, out_path)
