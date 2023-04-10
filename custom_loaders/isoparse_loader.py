from dtale.cli.clickutils import get_loader_options

'''
  IMPORTANT!!! This global variable is required for building any customized CLI loader.
  When find loaders on startup it will search for any modules containing the global variable LOADER_KEY.
'''
LOADER_KEY = 'isoparse'
LOADER_PROPS = []


# IMPORTANT!!! This function is required for building any customized CLI loader.
def find_loader(kwargs):
    if kwargs.get('isoparse', False):
        def _testdata_loader():
            import pandas as pd
            from dateutil.parser import isoparse

            return pd.DataFrame(dict(
                x=['a', 'b', 'c'],
                y=[isoparse(x) for x in ['2021-01-01', '2021-01-02', '2021-01-03']]
            ))

        return _testdata_loader
    return None