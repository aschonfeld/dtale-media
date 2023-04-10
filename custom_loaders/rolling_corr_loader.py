from dtale.cli.clickutils import get_loader_options
from dtale.views import startup

'''
  IMPORTANT!!! This global variable is required for building any customized CLI loader.
  When find loaders on startup it will search for any modules containing the global variable LOADER_KEY.
'''
LOADER_KEY = 'rolling_corr'
LOADER_PROPS = [dict(name='type')]


# IMPORTANT!!! This function is required for building any customized CLI loader.
def find_loader(kwargs):
    rolling_opts = get_loader_options(LOADER_KEY, LOADER_PROPS, kwargs)
    if len([f for f in rolling_opts.values() if f]):
        def _testdata_loader():
            import pandas as pd
            import numpy as np

            if rolling_opts['type'] == 'timestamp':
                ii = pd.date_range(start="2018-01-01", periods=700, freq="T")
            elif rolling_opts["type"] == "non-date":
                data = np.random.random((16000, 5))
                data = pd.DataFrame(data)
                data.index = [1] * len(data)
                return data
            else:
                ii = pd.date_range(start="2018-01-01", end="2019-12-01", freq="D")
            ii = pd.Index(ii, name="date")
            n = ii.shape[0]
            c = 5
            data = np.random.random((n, c))

            # startup(data=pd.DataFrame([1, 2, 3, 4]), ignore_duplicate=True)
            # startup(data=pd.DataFrame([5, 6, 7, 8]), ignore_duplicate=True)

            return pd.DataFrame(data, index=ii)

        return _testdata_loader
    return None