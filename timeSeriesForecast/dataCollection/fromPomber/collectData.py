import requests
import json
import pprint

response = requests.get("https://pomber.github.io/covid19/timeseries.json")
responseInJson = response.json()
with open('data.json', 'w') as f:
    json.dump(responseInJson, f)

with open('data.json', 'r') as p:
    data = p.read()
    json_data = json.loads(data)
pprint.pprint(json_data)    
