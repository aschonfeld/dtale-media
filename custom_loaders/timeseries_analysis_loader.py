from dtale.cli.clickutils import get_loader_options
from dtale.views import startup

'''
  IMPORTANT!!! This global variable is required for building any customized CLI loader.
  When find loaders on startup it will search for any modules containing the global variable LOADER_KEY.
'''
LOADER_KEY = 'timeseries_analysis'
LOADER_PROPS = []


# IMPORTANT!!! This function is required for building any customized CLI loader.
# http://0.0.0.0:9206/dtale/timeseries-analysis/1?type=hpfilter&cfg=%7B%22col%22%3A%22realgdp%22%2C%22index%22%3A%22index%22%7D
def find_loader(kwargs):
    if kwargs.get('timeseries_analysis', False):
        def _testdata_loader():
            import pandas as pd
            import statsmodels.api as sm

            dta = sm.datasets.macrodata.load_pandas().data
            index = pd.period_range('1959Q1', '2009Q3', freq='Q')
            dta = dta.set_index(index)
            dta.index.name = 'date'
            return dta

        return _testdata_loader
    return None