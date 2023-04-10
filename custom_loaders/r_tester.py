import rpy2.robjects as ro
from rpy2.robjects.packages import importr
from rpy2.robjects import pandas2ri

from rpy2.robjects.conversion import localconverter

pandas2ri.activate()

if __name__ == '__main__':
    base = importr('base')
    base.load('/Users/andrewschonfeld/Downloads/dslabs/data/movielens.rda')
    with localconverter(ro.default_converter + pandas2ri.converter):
        dataset = base.get('movielens')
        r_from_pd_df = ro.conversion.py2rpy(dataset)
        print(r_from_pd_df.head())
