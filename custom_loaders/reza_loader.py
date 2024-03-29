from dtale.cli.clickutils import get_loader_options

'''
  IMPORTANT!!! This global variable is required for building any customized CLI loader.
  When find loaders on startup it will search for any modules containing the global variable LOADER_KEY.
'''
LOADER_KEY = 'reza-data'
LOADER_PROPS = []


# IMPORTANT!!! This function is required for building any customized CLI loader.
def find_loader(kwargs):
    if kwargs.get('reza_data', False):
        def _testdata_loader():
            import os
            import pandas as pd

            fname = os.path.join(os.path.dirname(__file__), 'DemoData3.csv')
            data = pd.read_csv(fname, parse_dates=['DateAdded'])
            #data['Price'] = data['Price'].replace('[\$,]', '', regex=True).astype(float)
            return data

        return _testdata_loader
    return None