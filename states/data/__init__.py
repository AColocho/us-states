import importlib.resources
import json

with importlib.resources.path('data/states.json') as _states_file_:
    _states_data_ = json.loads(_states_file_.read())

with importlib.resources.path(".data","territories.json") as _territories_file_:
    _territories_data_ = json.loads(_territories_file_.read())
