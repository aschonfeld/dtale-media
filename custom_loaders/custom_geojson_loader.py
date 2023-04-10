from dtale.cli.clickutils import get_loader_options

'''
  IMPORTANT!!! This global variable is required for building any customized CLI loader.
  When find loaders on startup it will search for any modules containing the global variable LOADER_KEY.
'''
LOADER_KEY = 'custom-geojson-data'
LOADER_PROPS = []


# IMPORTANT!!! This function is required for building any customized CLI loader.
def find_loader(kwargs):
    if kwargs.get('custom_geojson_data', False):
        def _testdata_loader():
            import pandas as pd

            return pd.DataFrame([
                dict(id='US.MA', name='mass', pop=125),
                dict(id='US.WA', name='wash', pop=500),
                dict(id='US.CA', name='cali', pop=1000),
            ])

        return _testdata_loader
    return None