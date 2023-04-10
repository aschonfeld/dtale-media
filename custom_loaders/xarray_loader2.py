from dtale.cli.clickutils import get_loader_options

'''
  IMPORTANT!!! This global variable is required for building any customized CLI loader.
  When find loaders on startup it will search for any modules containing the global variable LOADER_KEY.
'''
LOADER_KEY = 'xarray2-data'
LOADER_PROPS = []


# IMPORTANT!!! This function is required for building any customized CLI loader.
def find_loader(kwargs):
    if kwargs.get('xarray2_data', False):
        def _testdata_loader():
            import xarray as xr

            return xr.open_dataset('/Users/andrewschonfeld/Downloads/roi.nc')

        return _testdata_loader
    return None