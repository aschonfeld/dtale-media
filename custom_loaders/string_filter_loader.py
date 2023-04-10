from dtale.cli.clickutils import get_loader_options

'''
  IMPORTANT!!! This global variable is required for building any customized CLI loader.
  When find loaders on startup it will search for any modules containing the global variable LOADER_KEY.
'''
LOADER_KEY = 'string_filter'
LOADER_PROPS = []


# IMPORTANT!!! This function is required for building any customized CLI loader.
def find_loader(kwargs):
    if kwargs.get('string_filter', False):
        def _testdata_loader():
            import pandas as pd

            return pd.DataFrame(dict(id=['foo', 'bar', 'baz']))

        return _testdata_loader
    return None