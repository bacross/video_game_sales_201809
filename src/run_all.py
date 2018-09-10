import cfg
import pandas as pd
from etl.extract_data_from_zip import extract_data_from_zip as edfz
from etl.get_kaggle import get_kaggle
from etl.munge_df import munge_df
from models import hier_reg as hr

### download kaggle data if necessary
if cfg.refresh_data_flag == True:
    get_kaggle(cfg.kaggle_cmd, cfg.raw_data_path)
    edfz(cfg.zip_file_path, cfg.zip_extract_path)

### load data into pandas data frame
df_vid_sales = pd.read_csv(cfg.csv_fpath)
df_vid_sales_com = munge_df(df_vid_sales)

### compile stan model
sm = hr.comp_stan(cfg.hier_stan_code)

### config stan model data
hier_data,df_vid_sales_com_train,df_vid_sales_com_test = hr.config_stan_data(df_vid_sales_com_train,hier_col_name ='Genre',frac=cfg.train_frac)

### fit stan model
fit = sm.sampling(data=hier_data)

### test out of sample fit
mad = hr.pred_oos(fit,df_vid_sales_com_test)
print(mad)

print('this is the end')
