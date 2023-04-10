from dtale.datasets import covid

'''
  IMPORTANT!!! This global variable is required for building any customized CLI loader.
  When find loaders on startup it will search for any modules containing the global variable LOADER_KEY.
'''
LOADER_KEY = 'ny-lottery'
LOADER_PROPS = []


# IMPORTANT!!! This function is required for building any customized CLI loader.
def find_loader(kwargs):
    if kwargs.get('ny_lottery', False):
        def ny_lottery():
            from dtale.cli.loaders.csv_loader import loader_func as load_csv

            data = load_csv(
                path="https://data.ny.gov/api/views/hsys-3def/rows.csv?accessType=DOWNLOAD&sorting=true"
            )
            return data
        return ny_lottery
    return None