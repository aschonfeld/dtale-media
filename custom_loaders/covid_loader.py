from dtale.cli.clickutils import get_loader_options
from dtale.cli.loaders.csv_loader import loader_func as load_csv

'''
  IMPORTANT!!! This global variable is required for building any customized CLI loader.
  When find loaders on startup it will search for any modules containing the global variable LOADER_KEY.
'''
LOADER_KEY = 'covid-data'
LOADER_PROPS = []


# IMPORTANT!!! This function is required for building any customized CLI loader.
def find_loader(kwargs):
    if kwargs.get('covid_data', False):
        def _testdata_loader():
            import pandas as pd

            data = load_csv(
                path='https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-states.csv',
                proxy='http://niproxy:8080',
                parse_dates=['date']
            )
            codes = load_csv(
                path='https://raw.githubusercontent.com/jasonong/List-of-US-States/master/states.csv',
                proxy='http://niproxy:8080',
            )
            codes = codes.set_index('State').to_dict()['Abbreviation']
            data['state_code'] = data['state'].map(codes)
            return data

        return _testdata_loader
    return None