import requests
import json
try:
    response = requests.get("http://api.open-notify.org/astros.json")
    response.raise_for_status()
except requests.exceptions.RequestException as e:  # This is the correct syntax
    raise SystemExit(e)
data = json.loads(response.text)
people = data['people']
names = []
for p in people:
    name = p['name']
    names.append(name)
print(sorted(names))