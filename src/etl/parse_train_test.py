import pandas as pd
import numpy as np

def parse_train_test(ndf,frac):
    train = ndf.sample(frac=frac)
    test = ndf.loc[~ndf.index.isin(train.index),:]
    return train,test