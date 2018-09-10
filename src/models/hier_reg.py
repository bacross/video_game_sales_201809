import pandas as pd
import pystan as ps
import numpy as np


def comp_stan(hier_stan_code):
    sm = ps.StanModel(model_code=hier_stan_code)
    return sm


def config_stan_data(ndata, hier_col_name):
    hier_names = ndata[hier_col_name].unique()
    hiers = len(hier_names)
    hier_lookup = dict(zip(hier_names, range(hiers)))
    hier = ndata['hier_code'] = ndata[hier_col_name].replace(hier_lookup).values
    hier_data = {'N': len(ndata.log_Global_Sales),
                 'J': hiers,
                 'hier': hier + 1,  # stan counts start at 1
                 'x': ndata.Critic_Score,
                 'y': ndata.log_Global_Sales}
    return hier_data


def fit_stan_model(hier_data):
    fit = ps.sampling(hier_data)
    return fit
