from dtale.cli.clickutils import get_loader_options

'''
  IMPORTANT!!! This global variable is required for building any customized CLI loader.
  When find loaders on startup it will search for any modules containing the global variable LOADER_KEY.
'''
LOADER_KEY = 'na2_test'
LOADER_PROPS = []


# IMPORTANT!!! This function is required for building any customized CLI loader.
def find_loader(kwargs):
    if kwargs.get('na2_test', False):
        def _testdata_loader():
            import pandas as pd
            import random

            dtypes = {
                "id": "uint64",
                "creation_time": "str",
                "timestamp": "str",
                "packet_type": "uint16",
                "psn": "uint16",
                "module": "uint16",
                "component": "uint16",
                "parameter": "uint16"
            }
            parse_dates = ["creation_time", "timestamp"]

            df = pd.read_csv("example_data.csv", dtype=dtypes, parse_dates=parse_dates)
            return df

        return _testdata_loader
    return None