from flask import redirect

import dtale
import pandas as pd
from dtale.app import build_app
from dtale.views import startup

if __name__ == '__main__':
    app = build_app(reaper_on=False)
    dtale.global_state.use_redis_store('/Users/andrewschonfeld/redis_test')

    @app.route("/create-df")
    def create_df():
        df = pd.DataFrame(dict(a=[1, 2, 3], b=[4, 5, 6]))
        instance = startup(data=df, ignore_duplicate=True)
        return redirect(f"/dtale/main/{instance._data_id}", code=302)

    @app.route("/")
    def hello_world():
        return 'Hi there, load data using <a href="/create-df">create-df</a>'

    app.run(host="0.0.0.0", port=8080)