
from etl import cleaning as cl
from etl import extraction as ex
from etl import feature_engineering as fe

def get_data():
    cl_data = cl.get_clean_data(ex.get_data())
    return fe.get_features(cl_data)