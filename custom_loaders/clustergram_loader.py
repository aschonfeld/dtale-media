from dtale.cli.clickutils import get_loader_options

'''
  IMPORTANT!!! This global variable is required for building any customized CLI loader.
  When find loaders on startup it will search for any modules containing the global variable LOADER_KEY.
'''
LOADER_KEY = 'clustergram'
LOADER_PROPS = []

# IMPORTANT!!! This function is required for building any customized CLI loader.
def find_loader(kwargs):
    if kwargs.get(LOADER_KEY, False):
        def _clustergram_loader():
            import pandas as pd

            return pd.read_csv(
                'https://raw.githubusercontent.com/plotly/dash-bio-docs-files/master/' +
                'clustergram_mtcars.tsv',
                sep='	', skiprows=4
            ).set_index('model')

        return _clustergram_loader
    return None
