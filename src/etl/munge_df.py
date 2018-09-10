import pandas as pd
from math import log
import numpy as np


def munge_df(ndf):
    ndf = ndf.replace('nan', np.nan)
    ndf = ndf.dropna()
    ndf['yrs_since'] = 2018 - ndf.Year_of_Release
    ndf['log_Global_Sales'] = ndf.Global_Sales.apply(lambda x: log(x))
    return ndf
