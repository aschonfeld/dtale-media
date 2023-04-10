from dtale.cli.clickutils import get_loader_options

'''
  IMPORTANT!!! This global variable is required for building any customized CLI loader.
  When find loaders on startup it will search for any modules containing the global variable LOADER_KEY.
'''
LOADER_KEY = 'cleaners'
LOADER_PROPS = []


# IMPORTANT!!! This function is required for building any customized CLI loader.
def find_loader(kwargs):
    if kwargs.get('cleaners', False):
        def _testdata_loader():
            import pandas as pd

            return pd.DataFrame.from_dict({
                'a': ['a999b', 'a999 b'],
                'c': ['Berlin200', 'Berlin 200'],
                'd': ['foo bar biz', 'foo bar'],
                'e': ["it's your's", "wu-tang"]
            })

        return _testdata_loader
    return None