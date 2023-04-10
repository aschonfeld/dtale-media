from dtale.cli.clickutils import get_loader_options

'''
  IMPORTANT!!! This global variable is required for building any customized CLI loader.
  When find loaders on startup it will search for any modules containing the global variable LOADER_KEY.
'''
LOADER_KEY = 'predefined_filters'
LOADER_PROPS = []


# IMPORTANT!!! This function is required for building any customized CLI loader.
def find_loader(kwargs):
    rolling_opts = get_loader_options(LOADER_KEY, LOADER_PROPS, kwargs)
    if len([f for f in rolling_opts.values() if f]):
        def _testdata_loader():
            import pandas as pd
            import dtale.predefined_filters as predefined_filters
            import dtale.global_state as global_state

            global_state.set_app_settings(dict(open_predefined_filters_on_startup=True))

            def filter1(df, val):
                print(val, type(val))
                print(df)
                print(df[(df["A"] == val)])
                print(df[(df["B"] > 2)])
                print(df[(df["A"] == val) & (df["B"] > 2)])
                return df[(df["A"] == val) & (df["B"] > 2)]

            predefined_filters.set_filters([
                {
                    "name": "A and B > 2",
                    "column": "A",
                    "description": "Filter A with B greater than 2",
                    # "handler": lambda df, val: df[(df["A"] == val) & (df["B"] > 2)],
                    "handler": filter1,
                    "input_type": "input",
                    "default": 1,
                    "active": True,
                },
                {
                    "name": "A and (B % 2) == 0",
                    "column": "A",
                    "description": "Filter A with B mod 2 equals zero (is even)",
                    "handler": lambda df, val: df[(df["A"] == val) & (df["B"] % 2 == 0)],
                    "input_type": "select",
                    "default": 1,
                    "active": False,
                },
                {
                    "name": "A in values and (B % 2) == 0",
                    "column": "A",
                    "description": "A is within a group of values and B mod 2 equals zero (is even)",
                    "handler": lambda df, val: df[df["A"].isin(val) & (df["B"] % 2 == 0)],
                    "input_type": "multiselect",
                    "default": [1],
                    "active": False,
                }
            ])

            return pd.DataFrame(
                ([[1, 2, 3, 4, 5, 6], [7, 8, 9, 10, 11, 12], [13, 14, 15, 16, 17, 18]]),
                columns=[
                    'A',
                    'B',
                    'C',
                    'D',
                    "E",
                    'F',
                ])

        return _testdata_loader
    return None