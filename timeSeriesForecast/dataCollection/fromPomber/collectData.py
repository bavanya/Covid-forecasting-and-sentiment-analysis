import requests
import json

response = requests.get("https://pomber.github.io/covid19/timeseries.json")
responseInJson = response.json()
with open('data.json', 'w') as f:
    json.dump(responseInJson, f)
