from dtale.cli.clickutils import get_loader_options

'''
  IMPORTANT!!! This global variable is required for building any customized CLI loader.
  When find loaders on startup it will search for any modules containing the global variable LOADER_KEY.
'''
LOADER_KEY = 'replacement-data'
LOADER_PROPS = []


# IMPORTANT!!! This function is required for building any customized CLI loader.
def find_loader(kwargs):
    if kwargs.get('replacement_data', False):
        def _testdata_loader():
            import pandas as pd
            import numpy as np

            return pd.DataFrame.from_dict({
                'a': ['a', 'UNknown', 'b'],
                'b': ['', ' ', ' - '],
                'c': [1, '', 3],
                'd': [1.1, np.nan, 3],
                'e': ['a', np.nan, 'b']
            })

        return _testdata_loader
    return None