from dtale.cli.clickutils import get_loader_options

'''
  IMPORTANT!!! This global variable is required for building any customized CLI loader.
  When find loaders on startup it will search for any modules containing the global variable LOADER_KEY.
'''
LOADER_KEY = 'issue-669-data'
LOADER_PROPS = []


# IMPORTANT!!! This function is required for building any customized CLI loader.
def find_loader(kwargs):
    if kwargs.get('issue_669_data', False):
        def _testdata_loader():
            from dtale.cli.loaders.csv_loader import loader_func

            return loader_func(
                path='https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv',
            )

        return _testdata_loader
    return None