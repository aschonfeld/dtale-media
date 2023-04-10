from dtale.cli.clickutils import get_loader_options
from dtale.views import startup

'''
  IMPORTANT!!! This global variable is required for building any customized CLI loader.
  When find loaders on startup it will search for any modules containing the global variable LOADER_KEY.
'''
LOADER_KEY = 'resample'
LOADER_PROPS = []


# IMPORTANT!!! This function is required for building any customized CLI loader.
def find_loader(kwargs):
    if kwargs.get('resample', False):
        def _testdata_loader():
            import pandas as pd
            import numpy as np

            start, end = '2000-10-01 23:30:00', '2000-10-03 00:30:00'
            rng = pd.date_range(start, end, freq='7min')
            ts = pd.Series(np.arange(len(rng)) * 3, index=rng)
            ts2 = pd.Series(np.arange(len(rng)) * 0.32, index=rng)
            return pd.DataFrame(data={'col1': ts, 'col2': ts2})

        return _testdata_loader
    return None