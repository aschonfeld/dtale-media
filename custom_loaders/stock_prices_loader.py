from dtale.cli.loaders.csv_loader import loader_func as load_csv

'''
  IMPORTANT!!! This global variable is required for building any customized CLI loader.
  When find loaders on startup it will search for any modules containing the global variable LOADER_KEY.
'''
LOADER_KEY = 'stock-prices'
LOADER_PROPS = []


# IMPORTANT!!! This function is required for building any customized CLI loader.
def find_loader(kwargs):
    if kwargs.get('stock_prices', False):
        def _loader():
            return load_csv(
                path='https://github.com/marcopeix/stock-prediction/raw/master/data/stock_prices_sample.csv'
            )
        return _loader
    return None