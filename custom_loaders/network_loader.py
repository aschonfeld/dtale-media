from dtale.cli.clickutils import get_loader_options

'''
  IMPORTANT!!! This global variable is required for building any customized CLI loader.
  When find loaders on startup it will search for any modules containing the global variable LOADER_KEY.
'''
LOADER_KEY = 'network'
LOADER_PROPS = []

# IMPORTANT!!! This function is required for building any customized CLI loader.
def find_loader(kwargs):
    if kwargs.get(LOADER_KEY, False):
        def _network_loader():
            import pandas as pd

            # return pd.DataFrame({
            #     "to": ["u2", "u3", "u1", "u4", "u5", "u6", "u7"],
            #     "from": ["u1", "u1", "u2", "u2", "u2", "u3", "u3"],
            #     "group": [1, 1, 1, 2, 2, 2, 3],
            # })
            return pd.read_csv("/Users/andrewschonfeld/dev/jupyterhub/NetworkX/input.csv")


        return _network_loader
    return None
