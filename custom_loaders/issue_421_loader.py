from dtale.cli.clickutils import get_loader_options

'''
  IMPORTANT!!! This global variable is required for building any customized CLI loader.
  When find loaders on startup it will search for any modules containing the global variable LOADER_KEY.
'''
LOADER_KEY = 'issue-421-data'
LOADER_PROPS = []


# IMPORTANT!!! This function is required for building any customized CLI loader.
def find_loader(kwargs):
    if kwargs.get('issue_421_data', False):
        def _testdata_loader():
            import pandas as pd

            df = pd.DataFrame({'year':[1992.0, 2005.0, 2011.0, 0.0, 2008.0, 1999.0, 1983.0, 2010.0, 0.0, 2002.0]})
            return df

        return _testdata_loader
    return None