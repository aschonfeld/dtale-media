from dtale.cli.clickutils import get_loader_options

'''
  IMPORTANT!!! This global variable is required for building any customized CLI loader.
  When find loaders on startup it will search for any modules containing the global variable LOADER_KEY.
'''
LOADER_KEY = 'microseconds'
LOADER_PROPS = []


# IMPORTANT!!! This function is required for building any customized CLI loader.
def find_loader(kwargs):
    rolling_opts = get_loader_options(LOADER_KEY, LOADER_PROPS, kwargs)
    if len([f for f in rolling_opts.values() if f]):
        def _testdata_loader():
            import pandas as pd
            from datetime import datetime as dt

            data = [{'A': 120, 'D': 1}, {'A': 122, 'B': 2.0}, {'A': 3, 'B': 3.0, 'D': 1}]
            tick_index = [dt(2013, 6, 1, 11, 00, 00, 0),
                          dt(2013, 6, 1, 11, 00, 00, 1),
                          dt(2013, 6, 1, 11, 00, 00, 2)]
            return pd.DataFrame(data, index=tick_index)

        return _testdata_loader
    return None