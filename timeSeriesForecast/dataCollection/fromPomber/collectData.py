import requests
import json
import pprint
import csv

response = requests.get("https://pomber.github.io/covid19/timeseries.json")
responseInJson = response.json()
with open('data.json', 'w') as f:
    json.dump(responseInJson, f)

with open('data.json', 'r') as p:
    data = p.read()
    json_parsed = json.loads(data)
pprint.pprint(json_parsed)    

json_data = json_parsed['India']
csv_data = open('csvData.csv', 'w')
csv_writer = csv.writer(csv_data)

count = 0

for day in json_data:
    if count == 0:
        header = day.keys()
        csv_writer.writerow(header)
        count+=1
    csv_writer.writerow(day.values())

csv_data.close()    
