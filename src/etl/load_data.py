import pandas as pd
import pickle


def load_data(csv_fpath,pickle_path,refresh_flag):
	if refresh_flag==True:
		df = pd_read_csv(csv_fpath)
		df.to_pickle(pickle_path)
	
	