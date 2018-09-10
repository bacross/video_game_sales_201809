import pandas as pd
import pystan as ps
import numpy as np


def comp_stan(hier_stan_code):
    sm = ps.StanModel(model_code=hier_stan_code)
    return sm

def parse_train_test(ndf,frac):
    train = ndf.sample(frac=frac)
    test = ndf.loc[~ndf.index.isin(train.index),:]
    return train,test

def config_stan_data(ndata, hier_col_name,frac):
    hier_names = ndata[hier_col_name].unique()
    hiers = len(hier_names)
    hier_lookup = dict(zip(hier_names, range(hiers)))
    hier = ndata['hier_code'] = ndata[hier_col_name].replace(hier_lookup).values
    ndata_train, ndata_test = parse_train_test(ndata,frac)
    hier_data = {'N': len(ndata_train.log_Global_Sales),
                 'J': hiers,
                 'hier': hier + 1,  # stan counts start at 1
                 'x': ndata_train.Critic_Score,
                 'y': ndata_train.log_Global_Sales}
    return hier_data, ndata_train,ndata_test

def fit_stan_model(hier_data):
    fit = ps.sampling(hier_data)
    return fit
    
def pred_oos(fit,df_vid_sales_com_test):
    a = fit['a'].mean(axis=0)
    b = fit['b'].mean(axis=0)
    x_pred = df_vid_sales_com_test.loc[:,['Critic_Score','hier_code']]
    y_pred = a[x_pred.hier_code] + b[x_pred.hier_code]*x_pred.Critic_Score
    resid = y_pred - df_vid_sales_com_test.log_Global_Sales
    abs_resid = resid.abs()
    mad = abs_resid.mean()
    return mad
    