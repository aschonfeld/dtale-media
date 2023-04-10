from dtale.cli.clickutils import get_loader_options

'''
  IMPORTANT!!! This global variable is required for building any customized CLI loader.
  When find loaders on startup it will search for any modules containing the global variable LOADER_KEY.
'''
LOADER_KEY = 'na_test'
LOADER_PROPS = []


# IMPORTANT!!! This function is required for building any customized CLI loader.
def find_loader(kwargs):
    if kwargs.get('na_test', False):
        def _testdata_loader():
            import pandas as pd
            import random

            s_int = pd.Series([random.randint(1, 100000000000) for _ in range(5)], index=list("abcde"), dtype=pd.Int64Dtype())
            s2_int = s_int.reindex(["a", "b", "c", "f", "u"])
            ints = pd.Series([random.randint(1, 100000000000) for _ in range(5)], index=list("abcfu"))
            df = pd.DataFrame(dict(na=s2_int, int=ints))
            df.loc[:, 'unsigned_int'] = pd.to_numeric(df['int'], downcast='unsigned')
            return df

        return _testdata_loader
    return None