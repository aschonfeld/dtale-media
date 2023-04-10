from dtale.cli.clickutils import get_loader_options
from dtale.views import startup

'''
  IMPORTANT!!! This global variable is required for building any customized CLI loader.
  When find loaders on startup it will search for any modules containing the global variable LOADER_KEY.
'''
LOADER_KEY = 'random-floats'
LOADER_PROPS = []


# IMPORTANT!!! This function is required for building any customized CLI loader.
def find_loader(kwargs):
    if kwargs.get('random_floats', False):
        def _testdata_loader():
            import pandas as pd
            import numpy as np

            return pd.DataFrame(np.random.randn(100, 2), columns=['col0', 'col1']) / 100

        return _testdata_loader
    return None