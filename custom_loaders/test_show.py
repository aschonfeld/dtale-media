import pandas as pd
import dtale
import dtale.global_state as global_state


if __name__ == "__main__":
    d = dtale.show(pd.DataFrame([1, 2, 3, 4, 5]), subprocess=True)

    global_state.set_app_settings(dict(hide_header_editor=True))

    dtale.show(pd.DataFrame([1, 2, 3, 4, 5]), subprocess=False, ignore_duplicate=True, hide_header_editor=True)

