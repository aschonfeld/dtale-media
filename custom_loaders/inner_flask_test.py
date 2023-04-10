import dtale
import pandas as pd
import time

from flask import Flask, redirect


if __name__ == '__main__':
    app = Flask(__name__)


    @app.route('/')
    def hello_world():
        if not len(dtale.global_state.get_data()):
            dtale.show(pd.DataFrame([1, 2, 3, 4, 5]))
        return 'Hello, World!'


    @app.route('/create-dtale')
    def create_dtale():
        if not len(dtale.global_state.get_data()):
            d = dtale.show(pd.DataFrame([1, 2, 3, 4, 5]))
            retries = 0
            while not d.is_up() and retries < 10:
                time.sleep(0.01)
                retries += 1

        return redirect(dtale.get_instance('1')._main_url, code=302)

    app.run(host='0.0.0.0', port=8080)
