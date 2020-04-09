from dtale.cli.clickutils import get_loader_options

'''
  IMPORTANT!!! This global variable is required for building any customized CLI loader.
  When find loaders on startup it will search for any modules containing the global variable LOADER_KEY.
'''
LOADER_KEY = 'trump-tweets'
LOADER_PROPS = []


# IMPORTANT!!! This function is required for building any customized CLI loader.
def find_loader(kwargs):
    if kwargs.get('trump_tweets', False):
        def _testdata_loader():
            import pandas as pd

            data = pd.read_csv(
                '/NIcommon/data/no_snapshot/pdupuis/datasets/trump_tweets_20190212_to_20200212_basic.csv',
                parse_dates=['created_at']
            )
            return data

        return _testdata_loader
    return None