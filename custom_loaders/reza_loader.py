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
            import pandas as pd

            data = pd.read_csv(
                '/NIres/data/no_snapshot/aschonfeld/DemoData3.csv',
                parse_dates=['DateAdded']
            )
            #data['Price'] = data['Price'].replace('[\$,]', '', regex=True).astype(float)
            return data

        return _testdata_loader
    return None