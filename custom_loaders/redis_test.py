import dtale
import pandas as pd

from dtale.app import build_app

from dtale.views import startup
from flask import redirect, jsonify


if __name__ == '__main__':

    app = build_app(reaper_on=False)

    dtale.global_state.use_redis_store('/Users/andrewschonfeld/dtale_data')

    if not dtale.global_state.contains("1"):
        df = pd.DataFrame([1, 2, 3, 4, 5])
        startup(data=df, data_id=1)


    @app.route("/create-df")
    def create_df():
        df = pd.DataFrame(dict(a=[1, 2, 3], b=[4, 5, 6]))
        instance = startup(data=df, ignore_duplicate=True)

        return redirect("/dtale/main/{}".format(instance._data_id), code=302)


    @app.route("/")
    @app.route("/active-instances")
    def get_all_dtale_servers():
        instances = []
        for data_id in dtale.global_state.keys():
            data_obj = dtale.get_instance(data_id)
            metadata = dtale.global_state.get_metadata(data_id) or {}
            name = dtale.global_state.get_data_inst(data_id).name
            # convert pandas timestamp to python dateTime
            datetime = None
            if "start" in metadata:
                time = pd.Timestamp(metadata["start"], tz=None).to_pydatetime()
                datetime = time.strftime("%Y-%m-%d %H:%M:%S")
            instances.append(
                {
                    'id': data_id,
                    'name': name,
                    'url': data_obj.main_url(),
                    'datetime': datetime
                }
            )
        return jsonify(instances)


    app.run(host="0.0.0.0", port=8080)
