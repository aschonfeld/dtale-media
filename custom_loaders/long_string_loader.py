from dtale.cli.clickutils import get_loader_options

'''
  IMPORTANT!!! This global variable is required for building any customized CLI loader.
  When find loaders on startup it will search for any modules containing the global variable LOADER_KEY.
'''
LOADER_KEY = 'long_strings'
LOADER_PROPS = []

LONG_STRING = (
    "Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. "
    "Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. "
    "Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem. Nulla consequat massa quis enim. "
    "Donec pede justo, fringilla vel, aliquet nec, vulputate eget, arcu. In enim justo, rhoncus ut, "
    "imperdiet a, venenatis vitae, justo. Nullam dictum felis eu pede mollis pretium. Integer tincidunt. "
    "Cras dapibus. Vivamus elementum semper nisi. Aenean vulputate eleifend tellus. Aenean leo ligula, "
    "porttitor eu, consequat vitae, eleifend ac, enim. Aliquam lorem ante, dapibus in, viverra quis, "
    "feugiat a, tellus. Phasellus viverra nulla ut metus varius laoreet. Quisque rutrum. Aenean imperdiet. "
    "Etiam ultricies nisi vel augue. Curabitur ullamcorper ultricies nisi. Nam eget dui. Etiam rhoncus. "
    "Maecenas tempus, tellus eget condimentum rhoncus, sem quam semper libero, sit amet adipiscing sem "
    "neque sed ipsum. Nam quam nunc, blandit vel, luctus pulvinar, hendrerit id, lorem. Maecenas nec "
    "odio et ante tincidunt tempus. Donec vitae sapien ut libero venenatis faucibus. Nullam quis ante. "
    "Etiam sit amet orci eget eros faucibus tincidunt. Duis leo. Sed fringilla mauris sit amet nibh. "
    "Donec sodales sagittis magna. Sed consequat, leo eget bibendum sodales, augue velit cursus nunc,"
)

# IMPORTANT!!! This function is required for building any customized CLI loader.
def find_loader(kwargs):
    rolling_opts = get_loader_options(LOADER_KEY, LOADER_PROPS, kwargs)
    if len([f for f in rolling_opts.values() if f]):
        def _testdata_loader():
            import pandas as pd
            import random

            def build_string():
                pct = random.randint(0, 101)
                pct_len = int(len(LONG_STRING) * (pct / 100.0))
                return LONG_STRING[:pct_len]

            data = {
                c: [build_string() for i in range(35)] for c in 'ABCDEF'
            }
            return pd.DataFrame(data, columns=list('ABCDEF'))

        return _testdata_loader
    return None