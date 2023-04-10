from dtale.cli.clickutils import get_loader_options

'''
  IMPORTANT!!! This global variable is required for building any customized CLI loader.
  When find loaders on startup it will search for any modules containing the global variable LOADER_KEY.
'''
LOADER_KEY = 'issue-184-data'
LOADER_PROPS = []


# IMPORTANT!!! This function is required for building any customized CLI loader.
def find_loader(kwargs):
    if kwargs.get('issue_184_data', False):
        def _testdata_loader():
            import pandas as pd
            import numpy as np

            df = pd.DataFrame({
                'var1': ['a', np.nan, np.nan, np.nan, np.nan],
                'var2': [np.nan, 'b', np.nan, np.nan, np.nan],
                'var3': [np.nan, 'c', 'x', np.nan, np.nan],
                'var4': [np.nan, np.nan, np.nan, 'd', np.nan],
                'var5': [np.nan, np.nan, np.nan, np.nan, np.nan]
            })
            return df

        return _testdata_loader
    return None