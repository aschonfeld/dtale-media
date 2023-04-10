from dtale.cli.clickutils import get_loader_options

'''
  IMPORTANT!!! This global variable is required for building any customized CLI loader.
  When find loaders on startup it will search for any modules containing the global variable LOADER_KEY.
'''
LOADER_KEY = 'pareto'
LOADER_PROPS = []


# IMPORTANT!!! This function is required for building any customized CLI loader.
def find_loader(kwargs):
    if kwargs.get('pareto', False):
        def _testdata_loader():
            import pandas as pd

            return pd.DataFrame([
                {'desc': ' foo', 'count': 10, 'cum_pct': 15},
                {'desc': 'bar', 'count': 6, 'cum_pct': 40},
                {'desc': 'baz', 'count': 3, 'cum_pct': 75},
                {'desc': 'biz ', 'count': 1, 'cum_pct': 100}
            ])

        return _testdata_loader
    return None