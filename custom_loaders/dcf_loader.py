from dtale.cli.clickutils import get_loader_options

'''
  IMPORTANT!!! This global variable is required for building any customized CLI loader.
  When find loaders on startup it will search for any modules containing the global variable LOADER_KEY.
'''
LOADER_KEY = 'dcf'
LOADER_PROPS = []


# IMPORTANT!!! This function is required for building any customized CLI loader.
def find_loader(kwargs):
    if kwargs.get('dcf', False):
        def _testdata_loader():
            import pandas as pd

            years = ['2020A']
            sales = [31.0]
            growth_rate = 0.1

            for year in range(1, 6):
                suffix = 'B' if year == 1 else 'P'
                years.append('{}{}'.format(2020 + year, suffix))
                sales.append(sales[year - 1] * (1 + growth_rate))

            return pd.DataFrame(dict(year=years, sales=sales))

        return _testdata_loader
    return None