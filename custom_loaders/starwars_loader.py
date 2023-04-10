from dtale.cli.clickutils import get_loader_options

'''
  IMPORTANT!!! This global variable is required for building any customized CLI loader.
  When find loaders on startup it will search for any modules containing the global variable LOADER_KEY.
'''
LOADER_KEY = 'starwars'
LOADER_PROPS = []


def read_json():
    import json
    import os
    import pandas as pd

    with open(os.path.join(os.path.dirname(__file__), "starwars-episode-4-interactions-allCharacters.json")) as f:
        js_graph = json.load(f)
        js_nodes = pd.DataFrame(js_graph["nodes"])
        js_links = pd.DataFrame(js_graph["links"])
        return js_nodes, js_links


# IMPORTANT!!! This function is required for building any customized CLI loader.
def find_loader(kwargs):
    if kwargs.get(LOADER_KEY, False):
        def _starwars_loader():
            import pandas as pd

            nodes, links = read_json()
            nodes.index.name = "id"
            nodes = nodes.reset_index()

            name_map = nodes.set_index("id")["name"].to_dict()
            color_map = nodes.set_index("id")["colour"].to_dict()

            links.loc[:, "color"] = links["source"].apply(lambda x: color_map.get(x, x))
            links.loc[:, "source"] = links["source"].apply(lambda x: name_map.get(x, x))
            links.loc[:, "target"] = links["target"].apply(lambda x: name_map.get(x, x))
            return links
        return _starwars_loader
    return None
