from dtale.cli.clickutils import get_loader_options

'''
  IMPORTANT!!! This global variable is required for building any customized CLI loader.
  When find loaders on startup it will search for any modules containing the global variable LOADER_KEY.
'''
LOADER_KEY = 'mbta'
LOADER_PROPS = []


# IMPORTANT!!! This function is required for building any customized CLI loader.
def find_loader(kwargs):
    if kwargs.get('mbta', False):
        def _testdata_loader():
            import os
            import pandas as pd

            fname = os.path.join(os.path.dirname(__file__), 'mbta.csv')
            df = pd.read_csv(fname)
            from_stops = df[['route_id', 'direction_id', 'stop_name', 'stop_order', 'first_stop', 'last_stop']]
            from_stops = from_stops.rename(columns={'stop_name': 'from'})
            from_stops = from_stops.set_index(['route_id', 'direction_id', 'stop_order', 'first_stop', 'last_stop'])

            to_stops = df[['route_id', 'direction_id', 'stop_name', 'stop_order', 'first_stop', 'last_stop']]
            to_stops = to_stops.rename(columns={'stop_name': 'to'})
            to_stops.loc[:, 'stop_order'] = to_stops['stop_order'] - 1
            to_stops = to_stops.set_index(['route_id', 'direction_id', 'stop_order', 'first_stop', 'last_stop'])

            final = from_stops.merge(to_stops, left_index=True, right_index=True, how='inner')
            return final.reset_index()

        return _testdata_loader
    return None