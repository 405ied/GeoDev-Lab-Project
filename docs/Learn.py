import json
with open('states.json', encoding='utf-8-sig') as f:
    data = json.load(f)

print(type(data))
print(data['name'])
print(data['features'][0])