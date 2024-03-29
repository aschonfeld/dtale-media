import dtale


if __name__ == '__main__':
    from memory_profiler import profile


    def test_data(rows, columns, no_of_dates=364):
        import pandas as pd
        import numpy as np
        import random
        from past.utils import old_div
        from pandas.tseries.offsets import Day
        from dtale.utils import dict_merge
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

        def pp(start, end, n):
            start_u = start.value // 10 ** 9
            end_u = end.value // 10 ** 9
            return pd.DatetimeIndex((10 ** 9 * np.random.randint(start_u, end_u, n, dtype=np.int64)).view('M8[ns]'))

        data.loc[:, 'ts_val'] = pp(pd.Timestamp('19600101'), pd.Timestamp('20500101'), len(data))
        data.loc[:, 'timedelta_val'] = [datetime.timedelta(seconds=random.randint(1, 100000000)) for _ in
                                        range(len(data))]
        return data


    @profile
    def build_data():
        df = test_data(100, 1)
        return df.set_index(['date', 'security_id'])

    df = build_data()
    dtale.show(df, subprocess=False)
