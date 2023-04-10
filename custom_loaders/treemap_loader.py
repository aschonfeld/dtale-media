from dtale.cli.clickutils import get_loader_options

'''
  IMPORTANT!!! This global variable is required for building any customized CLI loader.
  When find loaders on startup it will search for any modules containing the global variable LOADER_KEY.
'''
LOADER_KEY = 'treemap'
LOADER_PROPS = []


# IMPORTANT!!! This function is required for building any customized CLI loader.
def find_loader(kwargs):
    if kwargs.get('treemap', False):
        def _testdata_loader():
            import pandas as pd

            volume = [350, 220, 170, 150, 50]
            labels = [
                'Liquid\n volume: 350k',
                'Savoury\n volume: 220k',
                'Sugar\n volume: 170k',
                'Frozen\n volume: 150k',
                'Non-food\n volume: 50k'
            ]
            dfs = []
            for g in ['group1', 'group2']:
                dfs.append(pd.DataFrame(dict(group=g, volume=volume, label=labels)))
            return pd.concat(dfs, ignore_index=True)

        return _testdata_loader
    return None