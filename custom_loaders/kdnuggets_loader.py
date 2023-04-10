from dtale.cli.clickutils import get_loader_options

'''
  IMPORTANT!!! This global variable is required for building any customized CLI loader.
  When find loaders on startup it will search for any modules containing the global variable LOADER_KEY.
'''
LOADER_KEY = 'kdnuggets'
LOADER_PROPS = []


# IMPORTANT!!! This function is required for building any customized CLI loader.
def find_loader(kwargs):
    if kwargs.get('kdnuggets', False):
        def _testdata_loader():
            import os
            import pandas as pd

            return pd.DataFrame(dict(
                a=[1, 1, 2, 2, 3, 3],
                b=[1, 2, 3, 4, 5, 6]
            ))

        return _testdata_loader
    return None