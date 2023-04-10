from dtale.cli.clickutils import get_loader_options
from dtale.views import startup

'''
  IMPORTANT!!! This global variable is required for building any customized CLI loader.
  When find loaders on startup it will search for any modules containing the global variable LOADER_KEY.
'''
LOADER_KEY = 'chinese-columns'
LOADER_PROPS = []


# IMPORTANT!!! This function is required for building any customized CLI loader.
def find_loader(kwargs):
    if kwargs.get('chinese_columns', False):
        def _testdata_loader():
            import numpy as np
            import pandas as pd

            return pd.DataFrame({
                '日期': ['2015-01-07', '2014-12-17', '2015-01-21', '2014-11-19', '2015-01-17',
                                      '2015-02-26', '2015-01-04', '2014-12-20', '2014-12-07', '2015-01-06'],
                '股票代码': ['600795', '600268', '002428', '600031', '002736', '600216', '000799', '601600',
                        '601939', np.nan]
            })

        return _testdata_loader
    return None