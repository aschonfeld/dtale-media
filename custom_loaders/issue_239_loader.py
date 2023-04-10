from dtale.cli.clickutils import get_loader_options

'''
  IMPORTANT!!! This global variable is required for building any customized CLI loader.
  When find loaders on startup it will search for any modules containing the global variable LOADER_KEY.
'''
LOADER_KEY = 'issue-239-data'
LOADER_PROPS = []


# IMPORTANT!!! This function is required for building any customized CLI loader.
def find_loader(kwargs):
    if kwargs.get('issue_239_data', False):
        def _testdata_loader():
            import pandas as pd

            data = {
                'mixed-integer1': [1, 2, 3, '-', 5, 6, 7, 8, '-', 10],
                'mixed-integer2': [1, 2, 3, '-', 5, 6, 7, 8, '-', 10],
                'mixed-integer3': [1, 2, 3, '-', 5, 6, 7, 8, '-', 10],
                'mixed': [True, False, '-', False, True, True, False, '-', False, True],
                'string_floats': ['1', '00', '1.05', ' ', ' ', '', '02', '..', 'none', 'nan']
            }
            return pd.DataFrame(data)

        return _testdata_loader
    return None