from urllib.request import urlopen
import json

url = 'https://cdn.jsdelivr.net/npm/vega-datasets@2.5.3/data/football.json'

data = urlopen(url)
data = json.loads(data.read())


leagues = []

for item in data:
    league = item['division']
    if league not in leagues:
        leagues.append(league)
        

    
print(leagues)