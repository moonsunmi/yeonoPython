import json
import pprint

with open('movies.json') as file:
    json_data = file.read()

data = json.loads(json_data)
pprint.pprint(data)