from dtale.cli.clickutils import get_loader_options

'''
  IMPORTANT!!! This global variable is required for building any customized CLI loader.
  When find loaders on startup it will search for any modules containing the global variable LOADER_KEY.
'''
LOADER_KEY = 'word_value_counts'
LOADER_PROPS = []


# IMPORTANT!!! This function is required for building any customized CLI loader.
def find_loader(kwargs):
    if kwargs.get('word_value_counts', False):
        def _testdata_loader():
            import pandas as pd

            return pd.DataFrame(dict(a=['a b c', 'd e f', 'g h i'], b=[3, 4, 5]))

        return _testdata_loader
    return None