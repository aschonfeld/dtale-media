from dtale.cli.clickutils import get_loader_options

'''
  IMPORTANT!!! This global variable is required for building any customized CLI loader.
  When find loaders on startup it will search for any modules containing the global variable LOADER_KEY.
'''
LOADER_KEY = 'split_or_merge_columns'
LOADER_PROPS = []


# IMPORTANT!!! This function is required for building any customized CLI loader.
def find_loader(kwargs):
    if kwargs.get('split_or_merge_columns', False):
        def _testdata_loader():
            import pandas as pd

            df = pd.DataFrame(dict(
                address=['152 shaw street', '913 parkview drive', '1299 folkstone drive'],
            ))
            df.loc[:, 'date'] = pd.Timestamp('now').date()
            df.loc[:, 'time'] = pd.Timestamp('now').time()
            return df

        return _testdata_loader
    return None