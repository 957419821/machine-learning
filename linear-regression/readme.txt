environment: Ubuntu16.04

generate_datas_for_linear_regression.py
	data will be stored into datas.txt

getDatasFromTxt.py
	get data from datas.txt, and return x & y,
	used by module linear_regression.py

linear_regression.py
	prototype of models created by generate_models.sh
	contains BGD, SGD, MGD

generate_models.sh
	create models according to linear_regression.py
	models will be named by model1.py, model2.py ... model10.py

execute_these_models.sh
	get these models, and execute them
	results will be stored into log.txt
