# -*- coding: utf-8 -*-
"""
Created on Thu Apr 12 09:47:10 2018

@author: jiangxingqi
"""

import cueb

category_file_path = "/Sourcedata/Codetable/variety.txt"

stand_path = "stand"

index_path = "index"

cueb.index_extract.index_extract_function(category_file_path,'stand','index')
#cueb.index_extract.index_extract_function('source/variety.txt', 'stand', 'index')