import pandas as pd
from pandas import DataFrame

feat= pd.read_csv('csv/UNSWB_raw_dataset/NUSW-NB15_features.csv', low_memory=False)
column_names = feat['Name'].str.strip().replace({'Label': 'label', 'ct_src_ ltm': 'ct_src_ltm'}).tolist()

r= pd.read_csv('csv/UNSWB_raw_dataset/UNSW-NB15_1.csv', header=None, names=column_names, low_memory=False)

def get_data()->DataFrame:
    return r

def get_head()->DataFrame:
    return feat.iloc[:,1]

def get_stats()->DataFrame:
    return r.describe()

def print_types():
    print(r.dtypes.sum)

def print_shape():
    print(r.shape)