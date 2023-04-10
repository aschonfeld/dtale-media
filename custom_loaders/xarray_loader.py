from dtale.cli.clickutils import get_loader_options

'''
  IMPORTANT!!! This global variable is required for building any customized CLI loader.
  When find loaders on startup it will search for any modules containing the global variable LOADER_KEY.
'''
LOADER_KEY = 'xarray-data'
LOADER_PROPS = []


# IMPORTANT!!! This function is required for building any customized CLI loader.
def find_loader(kwargs):
    if kwargs.get('xarray_data', False):
        def _testdata_loader():
            import numpy as np
            import pandas as pd
            import xarray as xr

            np.random.seed(123)

            xr.set_options(display_style="html")

            times = pd.date_range("2000-01-01", "2001-12-31", name="time")
            annual_cycle = np.sin(2 * np.pi * (times.dayofyear.values / 365.25 - 0.28))

            base = 10 + 15 * annual_cycle.reshape(-1, 1)
            tmin_values = base + 3 * np.random.randn(annual_cycle.size, 3)
            tmax_values = base + 10 + 3 * np.random.randn(annual_cycle.size, 3)

            return xr.Dataset(
                {
                    "tmin": (("time", "location"), tmin_values),
                    "tmax": (("time", "location"), tmax_values),
                },
                {"time": times, "location": ["IA", "IN", "IL"]},
            )

        return _testdata_loader
    return None