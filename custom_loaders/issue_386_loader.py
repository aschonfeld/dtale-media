# coding=utf-8
from dtale.cli.clickutils import get_loader_options

'''
  IMPORTANT!!! This global variable is required for building any customized CLI loader.
  When find loaders on startup it will search for any modules containing the global variable LOADER_KEY.
'''
LOADER_KEY = 'issue-386-data'
LOADER_PROPS = []


# IMPORTANT!!! This function is required for building any customized CLI loader.
def find_loader(kwargs):
    if kwargs.get('issue_386_data', False):
        def _testdata_loader():
            import pandas as pd

            df = pd.DataFrame({
                'var1': ['123', 'تست', 'foo123', 'fooÀ', '\u200c']
            })
            return df

        return _testdata_loader
    return None