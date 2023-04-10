from dtale.cli.clickutils import get_loader_options

'''
  IMPORTANT!!! This global variable is required for building any customized CLI loader.
  When find loaders on startup it will search for any modules containing the global variable LOADER_KEY.
'''
LOADER_KEY = 'duplicates'
LOADER_PROPS = []


# IMPORTANT!!! This function is required for building any customized CLI loader.
def find_loader(kwargs):
    if kwargs.get('duplicates', False):
        def _testdata_loader():
            import pandas as pd

            return pd.DataFrame(dict(
                Foo=[1, 2, 3, 4, 5],
                foo=[1, 2, 3, 4, 5],
                fOo=[4, 5, 6, 7, 8],
                foO=[4, 4, 4, 4, 4],
                bar=[5, 5, 5, 6, 6]
            ))

        return _testdata_loader
    return None