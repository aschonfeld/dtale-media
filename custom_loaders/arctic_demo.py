import dtale
import pandas as pd
# this is required if you have pandas >= 1.2 becuase arctic has some poor importing
pd.Panel = None

if __name__ == "__main__":
    from arctic import Arctic
    from arctic.date import mktz
    from datetime import datetime as dt

    db = Arctic("localhost")
    data = [{'A': 120, 'D': 1}, {'A': 122, 'B': 2.0}, {'A': 3, 'B': 3.0, 'D': 1}]
    # note, the tick index does not have to be sorted.  Arctic will sort it for you on reads
    tick_index = [dt(2013, 6, 1, 11, 00, 00, 0, tzinfo=mktz('UTC')),
                  dt(2013, 6, 1, 11, 00, 00, 1, tzinfo=mktz('UTC')),
                  dt(2013, 6, 1, 11, 00, 00, 2, tzinfo=mktz('UTC'))]
    data = pd.DataFrame(data, index=tick_index)
    if db.library_exists("tickdb"):
        db.delete_library("tickdb")
    db.initialize_library("tickdb", "TickStoreV3")
    lib = db.get_library("tickdb")
    lib.write("test", data)

    # you can add additional data just by calling "write" on the same symbol
    data2 = pd.DataFrame([{'A': 123, 'B': 4.0, 'D': 1}], index=[dt(2013, 6, 1, 11, 00, 00, 3, tzinfo=mktz('UTC'))])
    lib.write("test", data2)
    d = dtale.show(lib.read("test"), subprocess=False, open_browser=True)
