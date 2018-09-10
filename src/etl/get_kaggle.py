import os

def get_kaggle(kaggle_cmd,data_path):
	os_script = kaggle_cmd+' -p '+data_path
	os.system(os_script)
	print('kaggle data downloaded')
	