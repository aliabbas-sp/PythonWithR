from rpy2.robjects import pandas2ri
import rpy2.robjects as ro


def rpy2_to_pandas(rpy2_dataframe):
    pandas2ri.activate()
    pandas_dataframe = ro.conversion.rpy2py(rpy2_dataframe)
    return pandas_dataframe
