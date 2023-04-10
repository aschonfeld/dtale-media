from dtale.cli.clickutils import get_loader_options

'''
  IMPORTANT!!! This global variable is required for building any customized CLI loader.
  When find loaders on startup it will search for any modules containing the global variable LOADER_KEY.
'''
LOADER_KEY = 'gage_rnr'
LOADER_PROPS = []


# IMPORTANT!!! This function is required for building any customized CLI loader.
def find_loader(kwargs):
    if kwargs.get('gage_rnr', False):
        def _testdata_loader():
            import pandas as pd
            import dtale.global_state as global_state

            global_state.set_app_settings(dict(hide_drop_rows=True))

            return pd.DataFrame(
                [
                    [1, 1, 3.29, 3.41, 3.64],
                    [1, 2, 2.44, 2.32, 2.42],
                    [1, 3, 4.34, 4.17, 4.27],
                    [1, 4, 3.47, 3.5, 3.64],
                    [1, 5, 2.2, 2.08, 2.16],
                    [2, 1, 3.08, 3.25, 3.07],
                    [2, 2, 2.53, 1.78, 2.32],
                    [2, 3, 4.19, 3.94, 4.34],
                    [2, 4, 3.01, 4.03, 3.2],
                    [2, 5, 2.44, 1.8, 1.72],
                    [3, 1, 3.04, 2.89, 2.85],
                    [3, 2, 1.62, 1.87, 2.04],
                    [3, 3, 3.88, 4.09, 3.67],
                    [3, 4, 3.14, 3.2, 3.11],
                    [3, 5, 1.54, 1.93, 1.55]
                ],
                columns=['o', 'p', 'm1', 'm2', 'm3']
            )

        return _testdata_loader
    return None