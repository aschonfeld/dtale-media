from dtale.cli.clickutils import get_loader_options

'''
  IMPORTANT!!! This global variable is required for building any customized CLI loader.
  When find loaders on startup it will search for any modules containing the global variable LOADER_KEY.
'''
LOADER_KEY = 'candlestick'
LOADER_PROPS = []


# IMPORTANT!!! This function is required for building any customized CLI loader.
def find_loader(kwargs):
    if kwargs.get('candlestick', False):
        def _testdata_loader():
            import pandas as pd
            import pandas_datareader as pdr
            from datetime import datetime
            tiingo_key = 'ea2c8f3a3e859cb2af38c2e798e13bea0a0663c8'
            goog = pdr.get_data_tiingo('GOOG', api_key=tiingo_key, start=datetime(2020, 6, 1), end=datetime(2020, 8, 8))
            amzn = pdr.get_data_tiingo('AMZN', api_key=tiingo_key, start=datetime(2020, 6, 1), end=datetime(2020, 8, 8))
            return pd.concat([goog, amzn])

        return _testdata_loader
    return None