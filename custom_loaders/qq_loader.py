from dtale.cli.clickutils import get_loader_options

'''
  IMPORTANT!!! This global variable is required for building any customized CLI loader.
  When find loaders on startup it will search for any modules containing the global variable LOADER_KEY.
'''
LOADER_KEY = 'qq'
LOADER_PROPS = []


# IMPORTANT!!! This function is required for building any customized CLI loader.
def find_loader(kwargs):
    if kwargs.get('qq', False):
        def _testdata_loader():
            import pandas as pd
            import numpy as np

            measurements = np.random.normal(loc=20, scale=5, size=100)
            return pd.DataFrame(dict(test=measurements))

        return _testdata_loader
    return None