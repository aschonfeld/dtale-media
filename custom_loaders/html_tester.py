from dtale.cli.clickutils import get_loader_options

'''
  IMPORTANT!!! This global variable is required for building any customized CLI loader.
  When find loaders on startup it will search for any modules containing the global variable LOADER_KEY.
'''
LOADER_KEY = 'html_tester'
LOADER_PROPS = []


# IMPORTANT!!! This function is required for building any customized CLI loader.
def find_loader(kwargs):
    if kwargs.get('html_tester', False):
        def _testdata_loader():
            import pandas as pd
            import numpy as np
            from dtale.views import startup
            import dtale.global_state as global_state

            df = pd.DataFrame(dict(a=[
                '<span style="font-weight: bold">FOO</span>',
                '<a href="http://www.espn.com" target="_blank">ESPN</a>',
                '<pre style="padding: 0; margin: auto;">HTML Code</pre>',
                '<img src="https://i.kym-cdn.com/photos/images/original/000/076/524/Haters.gif" />',
                np.nan
            ], b=[1, 2, 3, 4, np.nan]))
            startup(data=df, ignore_duplicate=True, data_id='1')
            formatting = {'a': {'fmt': {'html': True}}}
            global_state.set_settings('1', {'columnFormats': formatting, 'nanDisplay': '...'})
            global_state.set_app_settings(dict(max_column_width=100, max_row_height=100))

            return pd.DataFrame([1, 2, 3, 4, 5])

        return _testdata_loader
    return None

def test_code(df):
    # DISCLAIMER: 'df' refers to the data you passed in when calling 'dtale.show'

    import pandas as pd

    if isinstance(df, (pd.DatetimeIndex, pd.MultiIndex)):
        df = df.to_frame(index=False)

    # remove any pre-existing indices for ease of use in the D-Tale code, but this is not required
    df = df.reset_index().drop('index', axis=1, errors='ignore')
    df.columns = [str(c) for c in df.columns]  # update columns to strings in case they are numbers

    chart_data = pd.concat([
        pd.Series(df.set_index('created_at').index.to_period('M').to_timestamp(how='end').values, index=df.index,
                  name='created_at|M'),
        df['created_at'],
    ], axis=1)
    chart_data = chart_data.sort_values(['created_at|M'])
    chart_data = chart_data.rename(columns={'created_at|M': 'x'})
    chart_data_count = chart_data.groupby(['x'])[['created_at']].count()
    chart_data_count.columns = ['created_at|count']
    chart_data = chart_data_count.reset_index()
    chart_data = chart_data.dropna()

    import plotly.graph_objs as go

    charts = []
    charts.append(go.Bar(
        x=chart_data['x'],
        y=chart_data['created_at|count']
    ))
    figure = go.Figure(data=charts, layout=go.Layout({
        'barmode': 'group',
        'legend': {'orientation': 'h'},
        'title': {'text': 'Count of created_at by created_at (Monthly)'},
        'xaxis': {'title': {'text': 'created_at (Monthly)'}},
        'yaxis': {'tickformat': '.0f', 'title': {'text': 'Count of created_at'}, 'type': 'linear'}
    }))

    # If you're having trouble viewing your chart in your notebook try passing your 'chart' into this snippet:
    #
    # from plotly.offline import iplot, init_notebook_mode
    #
    # init_notebook_mode(connected=True)
    # chart.pop('id', None) # for some reason iplot does not like 'id'
    # iplot(chart)