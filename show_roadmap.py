import json

roadmap = json.load(open('roadmap.json'))

items = {}

for item in roadmap:
    items[item["slug"]] = item

for item in items:
    print(item, items[item]["dependencies"])


