from dtale.cli.clickutils import get_loader_options

'''
  IMPORTANT!!! This global variable is required for building any customized CLI loader.
  When find loaders on startup it will search for any modules containing the global variable LOADER_KEY.
'''
LOADER_KEY = 'complex_data'
LOADER_PROPS = []


# IMPORTANT!!! This function is required for building any customized CLI loader.
def find_loader(kwargs):
    rolling_opts = get_loader_options(LOADER_KEY, LOADER_PROPS, kwargs)
    if len([f for f in rolling_opts.values() if f]):
        def _testdata_loader():
            import pandas as pd

            data = [[1, 2, 3], {1: 'a', 2: 'b', 3: 'c'}, [1]]
            # data = [1, 2, [3]]
            s = pd.Series(data)
            return pd.DataFrame(s)

        return _testdata_loader
    return None