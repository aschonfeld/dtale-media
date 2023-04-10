from dtale.cli.clickutils import get_loader_options

'''
  IMPORTANT!!! This global variable is required for building any customized CLI loader.
  When find loaders on startup it will search for any modules containing the global variable LOADER_KEY.
'''
LOADER_KEY = 'issue-602-data'
LOADER_PROPS = []

# IMPORTANT!!! This function is required for building any customized CLI loader.
def find_loader(kwargs):
    if kwargs.get('issue_602_data', False):
        def _network_loader():
            import pandas as pd

            df = pd.read_csv(
                "/Users/andrewschonfeld/dev/git/dtale/custom_loaders/dates_for_andrew.csv",
            )
            df['fields.updated'] = df['fields.updated'].apply(pd.Timestamp)
            df['fields.resolutiondate'] = df['fields.resolutiondate'].apply(pd.Timestamp)
            return df


        return _network_loader
    return None
