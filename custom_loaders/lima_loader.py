from dtale.cli.clickutils import get_loader_options

'''
  IMPORTANT!!! This global variable is required for building any customized CLI loader.
  When find loaders on startup it will search for any modules containing the global variable LOADER_KEY.
'''
LOADER_KEY = 'daniel-lima'
LOADER_PROPS = []


# IMPORTANT!!! This function is required for building any customized CLI loader.
def find_loader(kwargs):
    if kwargs.get('daniel_lima', False):
        def _testdata_loader():
            import pandas as pd
            import numpy as np

            ii = pd.date_range(start='2018-01-01', end='2019-12-01', freq='D')
            ii = pd.Index(ii, name='date')

            n = ii.shape[0]
            c = 5
            data = np.random.random((n, c))

            return pd.DataFrame(data, index=ii)

        return _testdata_loader
    return None