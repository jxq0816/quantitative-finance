import cueb

#category_file_path = "/Sourcedata/Codetable/variety.txt"

category_file_path = 'source/variety.txt'

trend_0_path = 'result/rs-decision-tree/0'

trend_1_path = 'result/rs-decision-tree/1'

out_path = 'result/rs-decision-tree'


cueb.result_sort.result_sort_function(category_file_path, trend_0_path, out_path, '0')

cueb.result_sort.result_sort_function(category_file_path, trend_1_path, out_path, '1')