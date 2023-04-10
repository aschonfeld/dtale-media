from dtale.cli.clickutils import get_loader_options

'''
  IMPORTANT!!! This global variable is required for building any customized CLI loader.
  When find loaders on startup it will search for any modules containing the global variable LOADER_KEY.
'''
LOADER_KEY = 'odd_names'
LOADER_PROPS = []


# IMPORTANT!!! This function is required for building any customized CLI loader.
def find_loader(kwargs):
    rolling_opts = get_loader_options(LOADER_KEY, LOADER_PROPS, kwargs)
    if len([f for f in rolling_opts.values() if f]):
        def _testdata_loader():
            import pandas as pd
            import dtale.global_state as global_state

            global_state.set_app_settings(dict(max_column_width=100))

            column_names = [
                'A1. asdf',
                'Total Traffic(MB)',
                'Downlink TCP Retransmission Rate(%)',
                'b '*50,
                "c",
                'f-{"name":"test","para":{"name":"test?"}}',
                '-.:?\/|test',
            ]

            return pd.DataFrame(
                ([[i2 + (len(column_names) * i) for i2 in range(1, len(column_names) + 1)] for i in range(1, 4)]),
                columns=column_names,
            )

        return _testdata_loader
    return None