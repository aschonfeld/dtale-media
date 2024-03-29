from dtale.cli.clickutils import get_loader_options

'''
  IMPORTANT!!! This global variable is required for building any customized CLI loader.
  When find loaders on startup it will search for any modules containing the global variable LOADER_KEY.
'''
LOADER_KEY = 'testdata'
LOADER_PROPS = [dict(name='rows'), dict(name='columns')]


def test_data(rows, columns, no_of_dates=364):
    import pandas as pd
    import numpy as np
    import random
    from past.utils import old_div
    from pandas.tseries.offsets import Day
    from dtale.utils import dict_merge
    from dtale.views import startup
    import dtale.global_state as global_state
    import string
    import datetime

    now = pd.Timestamp(pd.Timestamp('now').date())
    dates = pd.date_range(now - Day(no_of_dates), now)
    num_of_securities = max(old_div(rows, len(dates)), 1)  # always have at least one security
    securities = [
        dict(security_id=100000 + sec_id, int_val=random.randint(1, 100000000000),
             str_val=random.choice(string.ascii_letters) * 5)
        for sec_id in range(num_of_securities)
    ]
    data = pd.concat([
        pd.DataFrame([dict_merge(dict(date=date), sd) for sd in securities])
        for date in dates
    ], ignore_index=True)[['date', 'security_id', 'int_val', 'str_val']]
    col_names = ['Col{}'.format(c) for c in range(columns)]
    data = pd.concat([data, pd.DataFrame(np.random.randn(len(data), columns), columns=col_names)], axis=1)
    data.loc[data['security_id'] == 100000, 'str_val'] = np.nan
    data.loc[:, 'bool_val'] = data.index % 2 == 0
    data.loc[:, 'category_val'] = data['str_val'].astype('category')
    data.loc[:, 'category_val2'] = data.index % 2
    data.loc[:, 'category_val2'] = data['category_val2'].astype('category')
    data.loc[:, 'object_val'] = data['str_val'].astype('object')
    data.loc[:, 'latitude'] = pd.Series([random.randint(-90, 90) for _ in range(len(data))])
    data.loc[:, 'longitude'] = pd.Series([random.randint(-180, 180) for _ in range(len(data))])

    def pp(start, end, n):
        start_u = start.value//10**9
        end_u = end.value//10**9
        return pd.DatetimeIndex((10**9*np.random.randint(start_u, end_u, n, dtype=np.int64)).view('M8[ns]'))

    data.loc[:, 'ts_val'] = pp(pd.Timestamp('19600101'), pd.Timestamp('20500101'), len(data))
    data.loc[:, 'timedelta_val'] = [datetime.timedelta(seconds=random.randint(1, 100000000)) for _ in range(len(data))]

    startup(data=data, ignore_duplicate=True, data_id='1')
    # formatting = {'Col0': {'fmt': "0.0000"}}
    # global_state.set_settings('1', {'backgroundMode': "lowVariance", 'columnFormats': formatting})
    global_state.set_settings('1', {
        "backgroundMode": "rangeHighlight",
        "rangeHighlight": {
            "all": {
              "active": True,
              "equals": {"active": False},
              "greaterThan": {"active": True, "color": {"a": 1, "b": 157, "g": 245, "r": 255}, "value": 0.5},
              "lessThan": {"active": False},
            }
        }
    })

    # startup(data=data, ignore_duplicate=True, data_id='1')
    # column_edit_options = {'category_val2': ['0', '1', '2']}
    # global_state.set_settings('1', {'column_edit_options': column_edit_options})

    # startup(data=data, ignore_duplicate=True, data_id='1', auto_hide_empty_columns=True)
    # startup(data=data, ignore_duplicate=True, data_id='1', highlight_filter=True)

    return data


# IMPORTANT!!! This function is required for building any customized CLI loader.
def find_loader(kwargs):
    test_data_opts = get_loader_options(LOADER_KEY, LOADER_PROPS, kwargs)
    if len([f for f in test_data_opts.values() if f]):
        def _testdata_loader():
            return test_data(int(test_data_opts.get('rows', 1000500)), int(test_data_opts.get('columns', 96)))

        return _testdata_loader
    return None