from dtale.cli.clickutils import get_loader_options

'''
  IMPORTANT!!! This global variable is required for building any customized CLI loader.
  When find loaders on startup it will search for any modules containing the global variable LOADER_KEY.
'''
LOADER_KEY = 'transform-data'
LOADER_PROPS = []


# IMPORTANT!!! This function is required for building any customized CLI loader.
def find_loader(kwargs):
    if kwargs.get('transform_data', False):
        def _testdata_loader():
            import pandas as pd

            def _data():
                for i in range(100):
                    a = i % 5
                    b = i % 3
                    c = i % 4
                    yield dict(a=a, b=b, c=c, i=i)

            return pd.DataFrame(list(_data()))

        return _testdata_loader
    return None